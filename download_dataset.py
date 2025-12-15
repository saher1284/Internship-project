from icrawler.builtin import BingImageCrawler
import os

categories = ["LED spotlight", "running shoes", "smartphone", "headphones", "desk lamp"]

num_train = 400
num_val = 100

for category in categories:
    train_dir = f"dataset/train/{category.replace(' ', '_')}"
    val_dir = f"dataset/validation/{category.replace(' ', '_')}"
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)

    print(f"Downloading training images for: {category}")
    train_crawler = BingImageCrawler(storage={'root_dir': train_dir})
    train_crawler.crawl(keyword=category, max_num=num_train)

    print(f"Downloading validation images for: {category}")
    val_crawler = BingImageCrawler(storage={'root_dir': val_dir})
    val_crawler.crawl(keyword=category, max_num=num_val)
