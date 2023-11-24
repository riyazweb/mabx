from bing_image_downloader import downloader
# Replace spaces in title with hyphens
top = input("enter:")

dog = top.replace(" ", "-")

    # Download images of dogs
downloader.download(f"{dog}", limit= 5, output_dir="images", adult_filter_off=True, force_replace=False, filter = "gif")
