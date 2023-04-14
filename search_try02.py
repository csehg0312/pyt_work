def binaris_kereses(listaban_keresni, query):
    bal, jobb = 0, len(listaban_keresni) - 1
    matches = []

    while bal <= jobb:
        kozep = (bal + jobb) // 2
        if query in listaban_keresni[kozep]:
            print(listaban_keresni[kozep].rfind(query))
            # Found a match
            matches.append(listaban_keresni[kozep])
            
            # Check if there are more matches to the bal
            for i in range(kozep-1, -1, -1):
                if query in listaban_keresni[i]:
                    print(listaban_keresni[i].rfind(query))
                    matches.insert(0, listaban_keresni[i])
                else:
                    break
            
            # Check if there are more matches to the jobb
            for i in range(kozep+1, len(listaban_keresni)):
                if query in listaban_keresni[i]:
                    print(listaban_keresni[i].rfind(query))
                    matches.append(listaban_keresni[i])
                else:
                    break
            
            return matches

        elif query < listaban_keresni[kozep]:
            jobb = kozep - 1
        else:
            bal = kozep + 1
    
    return matches

def search_list(listaban_keresni, query):
    sorted_list = sorted(listaban_keresni)
    matches = binaris_kereses(sorted_list, query)
    
    if len(matches) == 0:
        print(f"No matches found for query '{query}'.")
    else:
        print(f"{len(matches)} matches found for query '{query}':")
        for match in matches:
            print(match)
            
    return matches
