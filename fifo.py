def fifo_page_replacement(page_references, num_frames):
    page_frames = []  
    page_faults = 0

    for page in page_references:
        if page not in page_frames:  
            if len(page_frames) < num_frames:
                page_frames.append(page)  
            else:
                page_frames.pop(0)  
                page_frames.append(page)  
            page_faults += 1  

    return page_faults
    
# hit = 3 miss = 9 fames = 3
page_references = list("701203042303120")
num_frames = 3
print("Page : ", page_references, "\nPage Frames : ", num_frames)

page_fault = fifo_page_replacement(page_references, num_frames)
hit = len(page_references) - page_fault

print("\nTotal page faults:", page_fault, "\nMiss Ratio :", format((page_fault/len(page_references) * 100), ".2f"))
print("\nTotal page hit :", len(page_references) - page_fault, "\nHit Ratio :", format((hit/len(page_references) * 100), ".2f"))
