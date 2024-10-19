# Real-Time Video Automation System

### GitHub Repository:
[Real-Time Video Automation System](https://github.com/sudo-amancodes/real-time-video-automation-system)

## Overview
The Real-Time Video Automation System is a Python-based automation tool designed to scrape, download, and upload Twitch clips to YouTube in real-time. This system efficiently automates the entire process, allowing users to scrape Twitch video links from specific channels, download them, and upload them to a YouTube account. Logs of downloaded links are maintained to prevent redundant downloads.

## Features
- **Scraping**: Automatically scrapes Twitch clips from specified pages using Selenium and BeautifulSoup.
- **Video Downloading**: Downloads videos using `yt-dlp` with optimal video and audio settings.
- **YouTube Uploading**: Automates video uploads to YouTube with metadata using Selenium-based YouTube Uploader.
- **Logging**: Keeps track of downloaded video links to avoid duplicates.
- **Automated Cleanup**: Removes downloaded videos from local storage once they are uploaded.

## Technologies Used
- **Python**: Main programming language for the automation system.
- **Selenium**: Used to automate browser interactions for scraping and uploads.
- **BeautifulSoup4**: HTML parsing library to scrape video links.
- **yt-dlp**: Downloads videos from Twitch.
- **ffmpeg**: Used for processing video and audio formats.
- **Bash**: For scripting file handling and cleanup.

## How it Works
1. **Scraping Twitch Clips**: The system scrapes Twitch clips for a specific game or category based on date ranges.
2. **Downloading Videos**: The scraped video links are processed and downloaded locally using `yt-dlp` with predefined quality settings.
3. **Uploading to YouTube**: The downloaded videos are automatically uploaded to YouTube with the relevant metadata like title and creator information.
4. **Logging**: The system logs all downloaded video links to ensure no duplicates are processed.
5. **Cleanup**: After successful uploads, the videos are deleted from the local system to free up space.

## How to Run
1. **Clone the repository**:
   ```bash
   git clone https://github.com/sudo-amancodes/real-time-video-automation-system.git
   cd real-time-video-automation-system
   ```
2. Install necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Selenium WebDriver: Download the appropriate ChromeDriver for your system and ensure it is in your PATH.

4. Run the script:
   ```bash
   python real-time-video-automation-system.py
   ```
5. Customize Settings:

- You can adjust the scraping URL and other parameters in the scrap() function.
- Ensure YouTubeUploader credentials are set up for YouTube uploads.
