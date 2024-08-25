import pyshorteners

def shorten_url(url):
    # Initialize the Shortener
    s = pyshorteners.Shortener()

    # Shorten the URL
    short_url = s.tinyurl.short(url)
    
    return short_url

if __name__ == "__main__":
    url = input("Enter the URL to shorten: ")
    short_url = shorten_url(url)
    print(f"Shortened URL: {short_url}")
