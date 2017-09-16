---
layout:     post
title:      "最长不重复子串"
subtitle:   ""
date:       2017-09-10
author:     "brucechen"
header-img: "img/post-bg-code.jpg"
published: true
tags:
    - code
    - 算法
---

### Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solution:
使用数组存储字符的下标，从左向右遍历，如果存在下标不为零的值，移动当前指针到重复元素所指下标的下一个元素还是遍历

`public int lengthOfLongestSubstring(String s) {
        int[] exists = new int[300];
        int maxSub = 0;
        int curSub = 0;
        List<Character> cached = new ArrayList<Character>();
        char[] arrs = s.toCharArray();
        for(int i = 0; i < arrs.length; i ++){
            int index = (int)arrs[i];
            if(exists[index] != 0){
                maxSub = Math.max(maxSub, curSub);
                i = exists[index];
                exists = new int[300];
            }else{
                exists[index] = i;
                curSub ++;
            }
        }
        return maxSub;
    }`