# ODEGI CHRISTINE AWUOR
# SCT211-0093/2022

# The code below draws a saguaro cactus using for loops, string concatenation and string multiplication

def saguaro_cactus():
    # Parts of the saguaro
    top_line = " xxx    xxxxxx\n"
    middle_lines = "X---X  X"
    mid_first_part = "       X"

    # A list of backslashes and foward slashes
    foward_slashes = ["/", "//", "///", "////", "/////"]
    backslashes = ["\\", "\\\\", "\\\\\\", "\\\\\\\\", "\\\\\\\\\\"]
    tildes = "~~~~~~X"
    end_part = "       X~~~~~~X"

    cactus = top_line
    # Takes care of the top half of the cactus using string concatenation
    for i in range(5):
        cactus += middle_lines + foward_slashes[i] + "-" * (5 - i) + "X\n"
    cactus += " xxxxxxX" + tildes + "    xxx\n"

    # Takes care of the middle part of the cactus
    for i in range(5):
        cactus += mid_first_part + "-" * (5 - i) + backslashes[i] + "X  X---X\n"
    cactus += mid_first_part + tildes + "xxxxxx\n"

    # The final part of the cactus
    for _ in range(6):
        cactus += end_part + "\n"

    # Print the pattern
    print(cactus)

    return cactus


# Call the function
saguaro_cactus()
