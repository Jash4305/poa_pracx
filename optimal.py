def optimal_page_replacement(page_references, num_frames):
    page_frames = []
    page_faults = 0
    for page in page_references:
        if page not in page_frames:
            if len(page_frames) < num_frames:
                page_frames.append(page)
            else:
                future_references = page_references[page_references.index(page) + 1:]
                max_distance = 0
                victim_index = 0
                for i, frame in enumerate(page_frames):
                    if frame not in future_references:
                        page_frames.pop(i)
                        page_frames.append(page)
                        break
                    else:
                        distance = future_references.index(frame)
                        if distance > max_distance:
                            max_distance = distance
                            victim_index = i
                else:
                    page_frames.pop(victim_index)
                    page_frames.append(page)
            page_faults += 1
    return page_faults

# hit = 3 miss = 9 frames = 3
page_references = list("701203042303120")
num_frames = 3
print("Page : ", page_references, "\nPage Frames : ", num_frames)

page_fault = optimal_page_replacement(page_references, num_frames)
hit = len(page_references) - page_fault

print("\nTotal page faults:", page_fault, "\nMiss Ratio :", format((page_fault/len(page_references) * 100), ".2f"))
print("\nTotal page hit :", len(page_references) - page_fault, "\nHit Ratio :", format((hit/len(page_references) * 100), ".2f"))