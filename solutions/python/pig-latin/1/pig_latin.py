"""Advanced one, hard to understand"""

def translate(text):
    
    # result = []

    # for word in text.split():

    #     if (
    #         word.startswith(("a", "e", "i", "o", "u"))
    #         or word.startswith("xr")
    #         or word.startswith("yt")
    #     ):
    #         result.append(word + "ay")
    #         continue

    #     index = 0

    #     while index < len(word):
    #         if (
    #             word[index] in "aeiou"
    #             or (
    #                 word[index] == "y"
    #                 and index != 0
    #             )
    #         ):
    #             break

    #         if word[index:index + 2] == "qu":
    #             index += 2
    #             continue

    #         index += 1

    #     result.append(word[index:] + word[:index] + "ay")

    # return " ".join(result)

    result = []

    for word in text.split():

        """My version (seperated step by step with Flags as translated = true & false and break & continue words for sentence test"""

        translated = False

        """Rule 1"""
        for char in word:
            if (
                word[0].lower() in "aeiou"
                or word[0:2].lower() == "xr"
                or word[0:2].lower() == "yt"
            ):
                result.append(word + "ay")
                translated = True
                break

        if translated:
            continue


        """Rule 3"""
        rule_3 = 0
        for char in word:
            if word[rule_3:rule_3+2].lower() == "qu":
                result.append(word[rule_3+2:] + word[:rule_3+2] + "ay")
                translated = True
                break
            elif char.lower() in "bcdfghjklmnpqrstvwxyz":
                rule_3 += 1
            else:
                break
        if translated:
            continue
        

        """Rule 2"""
        rule_2 = 0
        for char in word:
            if char.lower() in "bcdfghjklmnpqrstvwxyz":
                rule_2 += 1
            else:
                result.append(word[rule_2:] + word[:rule_2] + "ay")
                translated = True
                break
        if translated:
            continue


        """Rule 4"""
        rule_4 = 0
        for char in word:
            if char.lower() in "bcdfghjklmnpqrstvwxz":
                rule_4 += 1
            elif word[rule_4].lower() == "y":
                result.append(word[rule_4:] + word[:rule_4] + "ay")
                tanslated = True
                break
                
            else:
                break
                
    return " ".join(result)



    



        
    
                
        

        
        


        
        
        
        
