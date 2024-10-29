import re
import Tokenizer as Token
from urllib.parse import urlparse, urlunparse, parse_qs
from bs4 import BeautifulSoup
from simhash import Simhash

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]

def extract_next_links(url, resp):
    # Implementation required.
    # url: the URL that was used to get the page
    # resp.url: the actual url of the page
    # resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
    # resp.error: when status is not 200, you can check the error here, if needed.
    # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
    #         resp.raw_response.url: the url, again
    #         resp.raw_response.content: the content of the page!
    # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content
    print(url)
    if resp is None or resp.raw_response is None or resp.status != 200:
        print("NoneType or Error")
        return []
    
    soup = BeautifulSoup(resp.raw_response.content, 'html.parser')
    tokens = Token.tokenize(soup.get_text())
    if len(tokens) < 10:
        print("low textual information")
        return []
    
    fingerprint = Simhash(tokens).value
    try:
        with open("fingerprints.txt", "r") as f:
            for line in f:
                old_fingerprint = int(line.strip())
                if bin(fingerprint ^ old_fingerprint).count("1") <= 3:
                    print("similar contents detected!")
                    return []
    except FileNotFoundError:
        pass

    with open("fingerprints.txt", "a") as f:
        f.write(f"{fingerprint}\n")

    freqs = Token.compute_word_frequencies(tokens)
    top_50_words = sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:50]
    
    print("The Top 50 Common Words:")
    for word, freq in top_50_words:
        print(f"{word} - {freq}")

    links = [link.get('href') for link in soup.find_all('a') if link.get('href') and is_valid(link.get('href'))]
    for i in range(len(links)):
        parsed = urlparse(links[i])
        links[i] = urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, ""))
    
    return links


def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    try:
        allowed_domains = ["ics.uci.edu","cs.uci.edu","informatics.uci.edu","stat.uci.edu"]
        allowed_specific_domain = "today.uci.edu"
        allowed_specific_path = "/department/information_computer_sciences"
        try:
            parsed = urlparse(url)
        except ValueError:
            return False
        
        if parsed.scheme not in set(["http", "https"]):
            return False
        if parsed.netloc == allowed_specific_domain and not parsed.path.startswith(allowed_specific_path):
            return False
        if not any(parsed.netloc.endswith(domain) for domain in allowed_domains):
            return False
        if "filter" in parsed.query and any("filter" in key for key in parse_qs(parsed.query)):
            return False
        return not re.search(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
