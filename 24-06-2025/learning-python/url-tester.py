def check_url():
    url = input("Enter the URL: ")
    url_is_found = True  # This is hardcoded; normally you'd check with requests or similar

    if url_is_found:
        return "URL is found"
    else:
        return "URL is not found"

# Call the function and print its result
print(check_url())
