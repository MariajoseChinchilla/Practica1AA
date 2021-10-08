def canConstruct(ransomNote, magazine):
    if len(magazine) < len(ransomNote):
        return False
    else:
        for letter in ransomNote:
            if letter not in magazine:
                return False
            if letter in magazine:
                magazine = magazine.replace(letter, '', 1)
                ransomNote = ransomNote.replace(letter,'',1)
            if ransomNote == '':
                return True

print(canConstruct('aab','baa'))