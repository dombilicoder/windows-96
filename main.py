import discord
from discord.ext import commands, tasks
import wavelink
import os
from dotenv import load_dotenv
import itertools
from aiohttp import web  # EKLENDİ: Render için web sunucusu kütüphanesi

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
VOICE_CHANNEL_ID = int(os.getenv("VOICE_CHANNEL_ID", 0))

durumlar = itertools.cycle([
    "w.yardım | Windows 96 devrede",
    "Kaset sarılıyor...",
    "Eskiyi özleyen herkese ithafen",
    "bir coZ projesi",
    "Nostalji rüzgarı esiyor..."
])

# --- EKLENDİ: RENDER İÇİN SAHTE WEB SUNUCUSU ---
async def web_server_handler(request):
    return web.Response(text="Windows 96 Sistemleri 7/24 Devrede! (bir coZ projesi)")

async def start_web_server():
    app = web.Application()
    app.router.add_get('/', web_server_handler)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render, portu otomatik olarak "PORT" çevresel değişkeninden verir. Bulamazsa 8080 kullanır.
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"🌐 Web sunucusu {port} portunda başlatıldı. Render bağlantısı başarılı!")
# ------------------------------------------------

class Windows96(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='w.', intents=intents, help_command=None)

    async def setup_hook(self):
        # EKLENDİ: Web sunucusunu arka planda asenkron olarak başlatıyoruz
        self.loop.create_task(start_web_server())

        for root, dirs, files in os.walk('./cmds'):
            for filename in files:
                if filename.endswith('.py') and not filename.startswith('__'):
                    path = os.path.join(root, filename)
                    module = path.replace('./', '').replace('/', '.').replace('\\', '.')[:-3]
                    await self.load_extension(module)
        
        host = os.getenv("LAVALINK_HOST")
        port = os.getenv("LAVALINK_PORT")
        password = os.getenv("LAVALINK_PASSWORD")
        secure_str = os.getenv("LAVALINK_SECURE", "false").lower()
        protocol = "https" if secure_str == "true" else "http"
        
        node = wavelink.Node(uri=f"{protocol}://{host}:{port}", password=password)
        await wavelink.Pool.connect(client=self, nodes=[node])

    async def on_ready(self):
        print(f'{self.user} olarak giriş yapıldı!')
        self.durum_degistir.start()
        self.embed_guncelleyici.start()
        
        if VOICE_CHANNEL_ID:
            channel = self.get_channel(VOICE_CHANNEL_ID)
            if channel:
                try:
                    await channel.connect(cls=wavelink.Player)
                except Exception as e:
                    print(f"Kanala katılırken hata: {e}")

    @tasks.loop(seconds=5)
    async def durum_degistir(self):
        await self.change_presence(activity=discord.Game(name=next(durumlar)))

    @tasks.loop(seconds=3)
    async def embed_guncelleyici(self):
        for guild in self.guilds:
            vc = guild.voice_client
            if vc and isinstance(vc, wavelink.Player) and getattr(vc, "aktif_mesaj", None):
                if vc.playing and vc.current:
                    try:
                        embed = vc.aktif_mesaj.embeds[0]
                        position = vc.position
                        length = vc.current.length
                        paused = vc.paused
                        
                        total_bars = 15
                        percentage = position / length if length > 0 else 0
                        filled = max(0, min(total_bars, int(percentage * total_bars)))
                        bar_list = ["-"] * total_bars
                        if 0 <= filled < total_bars:
                            bar_list[filled] = "•"
                        else:
                            bar_list[-1] = "•"
                        
                        p_min, p_sec = divmod(int(position / 1000), 60)
                        l_min, l_sec = divmod(int(length / 1000), 60)
                        emoji = "⏸️" if paused else "🎵"
                        
                        embed.description = f"{emoji} `{''.join(bar_list)}` `{p_min:02d}:{p_sec:02d}/{l_min:02d}:{l_sec:02d}`"
                        await vc.aktif_mesaj.edit(embed=embed)
                    except:
                        pass

bot = Windows96()

# Embed ve Track Event'leri (Öncekiyle Tamamen Aynı)
@bot.event
async def on_wavelink_track_start(payload: wavelink.TrackStartEventPayload):
    player = payload.player
    track = payload.track
    if not player or not hasattr(player, "metin_kanali"):
        return
        
    player.aktif_mesaj = None
    saniye = int(track.length / 1000)
    dakika, saniye = divmod(saniye, 60)
    sure_metni = f"{dakika}:{saniye:02d}"
    
    isteyen_uye = getattr(player, "guncel_isteyen", None)
    
    if isteyen_uye:
        footer_metni = f"İsteyen: {isteyen_uye.display_name} | Windows 96"
        profil_foto_url = isteyen_uye.display_avatar.url
    else:
        footer_metni = "İsteyen: Bilinmiyor | Windows 96"
        profil_foto_url = None
    
    embed = discord.Embed(
        title=f"🎶 {track.title}",
        url=track.uri,
        description=f"🎵 `•--------------` `00:00/{sure_metni}`",
        color=discord.Color.red()
    )
    embed.add_field(name="👤 Sanatçı", value=f"`{track.author}`", inline=True)
    embed.add_field(name="⏱️ Süre", value=f"`{sure_metni}`", inline=True)
    embed.add_field(name="🔊 Ses Seviyesi", value=f"`%{player.volume}`", inline=True)
    
    embed.set_footer(text=footer_metni, icon_url=profil_foto_url)
    
    if track.artwork:
        embed.set_image(url=track.artwork)
        
    try:
        player.aktif_mesaj = await player.metin_kanali.send(embed=embed)
    except:
        pass

@bot.event
async def on_wavelink_track_end(payload: wavelink.TrackEndEventPayload):
    player = payload.player
    track = payload.track
    if not player:
        return
        
    if getattr(player, "aktif_mesaj", None):
        try:
            embed = player.aktif_mesaj.embeds[0]
            length = track.length
            
            total_bars = 15
            bar_list = ["-"] * total_bars
            bar_list[-1] = "•"
            
            l_min, l_sec = divmod(int(length / 1000), 60)
            sure_metni = f"{l_min:02d}:{l_sec:02d}"
            
            embed.description = f"🏁 `{''.join(bar_list)}` `{sure_metni}/{sure_metni}`"
            embed.color = discord.Color.green()
            
            await player.aktif_mesaj.edit(embed=embed)
        except Exception as e:
            pass

    player.aktif_mesaj = None
    
    if not player.queue.is_empty:
        await player.play(player.queue.get())

if __name__ == "__main__":
    bot.run(TOKEN)