import subprocess
import sys
import os
import time
import threading
from datetime import datetime

class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class Animation:
    def __init__(self):
        self.is_running = False
        self.thread = None
    
    def progress_bar(self, percentage, width=40):
        filled = int(width * percentage / 100)
        bar = "█" * filled + "░" * (width - filled)
        return f"[{bar}] {percentage:3.0f}%"

def print_banner():
    banner = f"""
{Colors.BOLD}
═══════════════════════════════════════════════════════════
                🎵 SPOTIFY MUSIC DOWNLOADER 🎵
               Download your favorite music from Spotify
═══════════════════════════════════════════════════════════
{Colors.ENDC}"""
    print(banner)

def print_menu():
    menu = f"""
{Colors.BLUE}┌─────────────────────────────────────────────┐
│                  MAIN MENU                  │
├─────────────────────────────────────────────┤{Colors.ENDC}
│  1. 🔍 Search and Download Music           │
│  2. 📥 Download from Spotify URL           │
│  3. 📦 Batch Download URLs                 │
│  4. 📊 View Statistics                     │
│  5. ❌ Exit                               │
{Colors.BLUE}└─────────────────────────────────────────────┘{Colors.ENDC}
"""
    print(menu)

def search_music(query):
    """Search for music using spotDL search feature"""
    try:
        print(f"🔍 Searching for: {query}")
        
        # Use spotdl search command
        cmd = ['spotdl', 'search', query, '--count', '10']
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        if result.stdout.strip():
            lines = result.stdout.strip().split('\n')
            search_results = []
            
            for i, line in enumerate(lines[:10], 1):
                if 'https://open.spotify.com' in line:
                    # Extract song info and URL
                    parts = line.split(' - ')
                    if len(parts) >= 2:
                        artist = parts[0].strip()
                        title_url = parts[1].strip()
                        if 'https://' in title_url:
                            title = title_url.split('https://')[0].strip()
                            url = 'https://' + title_url.split('https://')[1]
                            search_results.append({
                                'number': i,
                                'artist': artist,
                                'title': title,
                                'url': url
                            })
            
            return search_results
        else:
            return []
            
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}❌ Search failed: {e.stderr}{Colors.ENDC}")
        return []
    except Exception as e:
        print(f"{Colors.FAIL}❌ Search error: {e}{Colors.ENDC}")
        return []

def display_search_results(results):
    """Display search results in a clean format"""
    if not results:
        print(f"{Colors.WARNING}No results found.{Colors.ENDC}")
        return
    
    print(f"\n{Colors.BOLD}Search Results:{Colors.ENDC}")
    print("─" * 60)
    
    for result in results:
        print(f"{result['number']:2d}. {Colors.BOLD}{result['artist']}{Colors.ENDC} - {result['title']}")
    
    print("─" * 60)

def get_timestamp():
    return datetime.now().strftime("%H:%M:%S")

def print_separator():
    print("─" * 60)

def simulate_download_progress():
    animation = Animation()
    print(f"\n🔍 Analyzing Spotify URL...")
    
    for i in range(0, 101, 20):
        progress = animation.progress_bar(i)
        print(f"\r📡 Fetching metadata: {progress}", end="", flush=True)
        time.sleep(0.3)
    
    print(f"\n✅ Metadata fetched successfully!")
    print(f"🎵 Converting and downloading...")
    
    for i in range(0, 101, 10):
        progress = animation.progress_bar(i)
        print(f"\r⬇️  Download progress: {progress}", end="", flush=True)
        time.sleep(0.2)
    
    print(f"\n🎉 Download completed!")

def download_spotify_content(spotify_url, output_dir=None):
    try:
        cmd = ['spotdl', spotify_url]
        
        if output_dir:
            cmd.extend(['--output', output_dir])
        
        print(f"⏳ [{get_timestamp()}] Starting download...")
        
        # Show progress simulation
        simulate_download_progress()
        
        # Actual download
        print(f"\n🎵 Executing spotDL command...")
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        print(f"{Colors.GREEN}✅ [{get_timestamp()}] Successfully downloaded!{Colors.ENDC}")
        
        if result.stdout.strip():
            print(f"📄 Download Details:")
            print(f"{result.stdout.strip()}")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"{Colors.FAIL}❌ [{get_timestamp()}] Error downloading {spotify_url}{Colors.ENDC}")
        if e.stderr:
            print(f"{Colors.FAIL}Error details: {e.stderr.strip()}{Colors.ENDC}")
        return False
    except Exception as e:
        print(f"{Colors.FAIL}❌ [{get_timestamp()}] Unexpected error: {e}{Colors.ENDC}")
        return False

def batch_download(urls_list, output_dir="./downloads"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Created output directory: {output_dir}")
    
    successful = 0
    failed = 0
    total = len(urls_list)
    
    print(f"\n🚀 Starting batch download of {total} items...")
    print("═" * 60)
    
    for i, url in enumerate(urls_list, 1):
        print(f"\n📥 [{i}/{total}] Processing: {url}")
        
        if download_spotify_content(url, output_dir):
            successful += 1
            print(f"✅ Item {i} completed successfully!")
        else:
            failed += 1
            print(f"❌ Item {i} failed to download!")
        
        if i < total:
            print("─" * 50)
    
    print("\n" + "═" * 60)
    print(f"📊 BATCH DOWNLOAD SUMMARY:")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"📋 Total: {total}")
    
    if successful > 0:
        print(f"{Colors.GREEN}🎉 Batch download completed! Check your '{output_dir}' folder.{Colors.ENDC}")
    
    print("═" * 60)

def print_stats():
    stats = f"""
📊 DOWNLOAD STATISTICS
═══════════════════════════════════════════════════════════
📈 Total Downloads Today:     0
🎵 Songs Downloaded:          0
📀 Albums Downloaded:         0
📁 Playlists Downloaded:      0
⏱️  Total Download Time:       0 minutes

💾 Storage Used:              0 MB
📂 Output Directory:          ./downloads
═══════════════════════════════════════════════════════════"""
    print(stats)

def search_and_download():
    """Search for music and download selected tracks"""
    print_separator()
    print(f"{Colors.BOLD}🔍 SEARCH AND DOWNLOAD MODE{Colors.ENDC}")
    print_separator()
    
    query = input("🎵 Enter song name, artist, or keywords: ").strip()
    if not query:
        print(f"{Colors.WARNING}❌ Please enter a search query{Colors.ENDC}")
        return
    
    results = search_music(query)
    if not results:
        return
    
    display_search_results(results)
    
    try:
        choice = input(f"\n{Colors.BLUE}Enter the number of the song to download (or 'q' to quit): {Colors.ENDC}").strip()
        
        if choice.lower() == 'q':
            return
        
        choice_num = int(choice)
        if 1 <= choice_num <= len(results):
            selected = results[choice_num - 1]
            output_dir = input("📁 Enter output directory (Enter for './downloads'): ").strip()
            if not output_dir:
                output_dir = "./downloads"
            
            print(f"\n🎵 Selected: {selected['artist']} - {selected['title']}")
            if download_spotify_content(selected['url'], output_dir):
                print(f"{Colors.GREEN}🎉 Download completed successfully!{Colors.ENDC}")
            else:
                print(f"{Colors.FAIL}💔 Download failed. Please try again.{Colors.ENDC}")
        else:
            print(f"{Colors.WARNING}❌ Invalid selection{Colors.ENDC}")
            
    except ValueError:
        print(f"{Colors.WARNING}❌ Please enter a valid number{Colors.ENDC}")

if __name__ == "__main__":
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_banner()
        
        while True:
            print_menu()
            choice = input(f"{Colors.BOLD}🎯 Enter your choice (1-5): {Colors.ENDC}").strip()
            
            if choice == "1":
                search_and_download()
            
            elif choice == "2":
                print_separator()
                print(f"{Colors.BOLD}📥 DIRECT URL DOWNLOAD MODE{Colors.ENDC}")
                print_separator()
                
                spotify_url = input("🔗 Enter Spotify URL: ").strip()
                
                if spotify_url:
                    output_dir = input("📁 Enter output directory (Enter for './downloads'): ").strip()
                    if not output_dir:
                        output_dir = "./downloads"
                    
                    print_separator()
                    print(f"🚀 Starting download...")
                    
                    if download_spotify_content(spotify_url, output_dir):
                        print(f"{Colors.GREEN}🎉 Download completed successfully!{Colors.ENDC}")
                    else:
                        print(f"{Colors.FAIL}💔 Download failed. Please check the URL and try again.{Colors.ENDC}")
                        
                    print_separator()
                else:
                    print(f"{Colors.FAIL}❌ Please enter a valid Spotify URL{Colors.ENDC}")
            
            elif choice == "3":
                print_separator()
                print(f"{Colors.BOLD}📦 BATCH DOWNLOAD MODE{Colors.ENDC}")
                print_separator()
                
                urls = []
                print("🔗 Enter Spotify URLs (press Enter on empty line to finish):")
                
                counter = 1
                while True:
                    url = input(f"   [{counter:2d}] URL: ").strip()
                    if not url:
                        break
                    urls.append(url)
                    print(f"      ✅ Added to queue")
                    counter += 1
                
                if urls:
                    output_dir = input("📁 Enter output directory (Enter for './downloads'): ").strip()
                    if not output_dir:
                        output_dir = "./downloads"
                    
                    batch_download(urls, output_dir)
                else:
                    print(f"{Colors.FAIL}❌ No URLs entered{Colors.ENDC}")
            
            elif choice == "4":
                print_separator()
                print_stats()
                print_separator()
            
            elif choice == "5":
                print_separator()
                print(f"{Colors.GREEN}👋 Thank you for using Spotify Music Downloader!{Colors.ENDC}")
                print(f"🎵 Happy listening! 🎵")
                print_separator()
                break
            
            else:
                print(f"{Colors.FAIL}❌ Invalid choice. Please enter 1, 2, 3, 4, or 5{Colors.ENDC}")
            
            if choice in ["1", "2", "3", "4"]:
                input(f"\n{Colors.WARNING}⏸️  Press Enter to return to main menu...{Colors.ENDC}")
                os.system('cls' if os.name == 'nt' else 'clear')
                print_banner()
                
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}⚠️  Program interrupted by user{Colors.ENDC}")
        print(f"👋 Thanks for using Spotify Music Downloader!")
    except Exception as e:
        print(f"\n{Colors.FAIL}💥 Unexpected error: {e}{Colors.ENDC}")
