# iterate through the referenced pages.
#   If the current page is already present in pages:
#       Remove the current page from pages.
#       Append the current page to the end of pages.
#       Increment page hits.
#   Else:
#       Increment page faults.
#       if pages contains fewer pages than its capacity s:
#           Append current page into pages.
#       else:
#           Remove the first page from pages.
#           Append the current page at the end of pages.
# Return the number of page hits and page faults.

def lru_page_replacement(page_references, num_frame):
    page_faults = 0
    page_frame = []
    for i in page_references:
        if i in page_frame:
            page_frame.remove(i)
            page_frame.append(i)
        else:
            page_faults += 1
            if len(page_frame) < num_frame:
                page_frame.append(i)
            else:
                page_frame.pop(0)
                page_frame.append(i)
    return page_faults

# hit = 3 miss = 10 fames = 3
page_references = list("701203042303120")
num_frames = 3
print("Page : ", page_references, "\nPage Frames : ", num_frames)

page_fault = lru_page_replacement(page_references, num_frames)
hit = len(page_references) - page_fault

print("\nTotal page faults:", page_fault, "\nMiss Ratio :", format((page_fault/len(page_references) * 100), ".2f"))
print("\nTotal page hit :", len(page_references) - page_fault, "\nHit Ratio :", format((hit/len(page_references) * 100),".2f"))
