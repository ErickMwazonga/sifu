'''
468. Validate IP Address
Link: https://leetcode.com/problems/validate-ip-address/

Given a string IP, return 'IPv4' if IP is a valid IPv4 address,
'IPv6' if IP is a valid IPv6 address or 'Neither' if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form 'x1.x2.x3.x4' where 0 <= xi <= 255 and xi cannot
contain leading zeros. For example, '192.168.1.1' and '192.168.1.0' are valid IPv4 addresses
but '192.168.01.1', while '192.168.1.00' and '192.168@1.1' are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form 'x1:x2:x3:x4:x5:x6:x7:x8' where:
1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits,
lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.

For example, '2001:0db8:85a3:0000:0000:8a2e:0370:7334' and '2001:db8:85a3:0:0:8A2E:0370:7334' 
are valid IPv6 addresses, while '2001:0db8:85a3::8A2E:037j:7334' and '02001:0db8:85a3:0000:0000:8a2e:0370:7334'
are invalid IPv6 addresses.

Examples
1. '172.16.254.1' -> 'IPv4'
2. '2001:0db8:85a3:0:0:8A2E:0370:7334' -> 'IPv6'
3. '256.256.256.256' ->'Neither'
4. '2001:0db8:85a3:0:0:8A2E:0370:7334:' -> 'Neither'
5. '1e1.4.5.6' -> 'Neither'
 
Constraints:
IP consists only of English letters, digits and the characters '.' and ':'
'''


class Solution:
    def validIPAddress(self, IP: str) -> str:
        if IP.count('.') == 3:
            if all(self.isIPv4(s) for s in IP.split('.')):
                return 'IPv4'

        if IP.count(':') == 7:
            if all(self.isIPv6(s) for s in IP.split(':')):
                return 'IPv6'

        return 'Neither'

    def isIPv4(self, s):
        try:
            num = int(s)
            return str(num) == s and 0 <= num <= 255
        except:
            return False

    def isIPv6(self, s):
        '''
        Binary - int('1010', 2)
        octal - int('12', 8)
        Hexadecimal - int('1010', 16)
        '''

        try:
            return len(s) <= 4 and int(s, 16) >= 0
        except:
            return False
