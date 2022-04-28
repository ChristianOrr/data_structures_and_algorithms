"""
You're given a string of length 12 or smaller, containing only digits.
Write a function that returns all the possible IP addresses that can be created by inserting three .s in the string.

An IP address is a sequence of four positive integers that are separated by .s,
where each individual integer is within the range 0 - 255, inclusive.

An IP address isn't valid if any of the individual integers contains leading 0s. For example,
"192.168.0.1" is a valid IP address, but "192.168.00.1" and "192.168.0.01" aren't,
because they contain "00" and 01, respectively.
Another example of a valid IP address is "99.1.1.10";
conversely, "991.1.1.0" isn't valid, because "991" is greater than 255.

Your function should return the IP addresses in string format and in no particular order.
If no valid IP addresses can be created from the string, your function should return an empty list.


Sample Input
string = "1921680"
Sample Output
[
  "1.9.216.80",
  "1.92.16.80",
  "1.92.168.0",
  "19.2.16.80",
  "19.2.168.0",
  "19.21.6.80",
  "19.21.68.0",
  "19.216.8.0",
  "192.1.6.80",
  "192.1.68.0",
  "192.16.8.0"
]
// The IP addresses could be ordered differently.
"""

def validIPAddresses(string):
    all_addresses = []
    for i in range(1, min(4, len(string) - 2)):
        ip = ["", "", "", ""]
        first_part = int(string[:i])
        ip[0] = string[:i]

        if first_part < 256 and str(first_part) == string[:i]:

            for j in range(i + 1, i + min(4, len(string[i:]))):
                second_part = int(string[i:j])
                ip[1] = string[i:j]

                if second_part < 256 and str(second_part) == string[i:j]:

                    for k in range(j + 1, j + min(4, len(string[j:]))):
                        third_part = int(string[j:k])
                        fourth_part = int(string[k:])
                        ip[2] = string[j:k]
                        ip[3] = string[k:]

                        if (third_part < 256 and str(third_part) == string[j:k]) and \
                                (fourth_part < 256 and str(fourth_part) == string[k:]):
                            all_addresses.append(".".join(ip))
    return all_addresses



if __name__ == "__main__":
    test = "1921680"
    out = validIPAddresses(test)
    print(f"The result is : {out}")
