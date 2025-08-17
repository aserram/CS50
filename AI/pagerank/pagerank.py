import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    d_per_link = 0
    if corpus[page]:
        d_per_link = damping_factor / len(corpus[page])
        rand_per_page = (1 - damping_factor) / (len(corpus))
    else:
        rand_per_page = 1 / (len(corpus))

    prob_dist = {}
    for element in corpus.keys():
        if element in corpus[page]:
            prob_dist[element] = d_per_link + rand_per_page
        else:
            prob_dist[element] = rand_per_page

    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    current_page = random.choice(list(corpus.keys()))
    pr = {page: 0 for page in corpus.keys()}

    for _ in range(n):
        model = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(list(model.keys()), list(model.values())).pop()
        pr[current_page] += 1

    pr = {k: v / n for k, v in pr.items()}
    return pr


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    prev_pr = {page: 1 / len(corpus) for page in corpus.keys()}
    next_pr = {page: 0 for page in corpus.keys()}
    not_converged = True

    while not_converged:
        for page_p in corpus.keys():
            prob_p = 0
            for page_i, links_i in corpus.items():
                if page_p in links_i:
                    prob_p += damping_factor * prev_pr[page_i] / len(links_i)
                elif not links_i:
                    prob_p += damping_factor * prev_pr[page_i] / len(corpus)

            next_pr[page_p] = ((1 - damping_factor) / len(corpus)) + prob_p

        for pr_prev, pr_next in zip(prev_pr.values(), next_pr.values()):
            not_converged = not_converged & (abs(pr_prev - pr_next) > 0.001)

        prev_pr = dict(next_pr)
    return next_pr


if __name__ == "__main__":
    main()
