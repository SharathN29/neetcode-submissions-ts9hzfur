class Solution {
    public boolean isAnagram(String s, String t) {
        int sLen = s.length();
        int tLen = t.length();

        if (sLen != tLen) return false; 

        Map<Character, Integer> charCount = new HashMap();

        for (int i = 0; i < sLen; i++) {
            charCount.put(s.charAt(i), charCount.getOrDefault(s.charAt(i), 0) + 1);
            charCount.put(t.charAt(i), charCount.getOrDefault(t.charAt(i), 0) - 1);
        }

        for (int n: charCount.values()) {
            if (n != 0) {
                return false;
            } 
        }

        return true;
    }
}
