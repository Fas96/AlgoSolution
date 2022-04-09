<h2><a href="https://leetcode.com/problems/top-k-frequent-elements/"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">347</font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">. </font></font><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Top K Frequent Elements</font></font></a></h2><h3>Medium</h3><hr><div><p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Given an integer array </font></font><code>nums</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> and an integer </font></font><code>k</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">, return </font></font><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">the</font></font></em> <code>k</code> <em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">most frequent elements</font></font></em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">. You may return the answer in </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">any order</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></p>

<p>&nbsp;</p>
<p><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Example 1:</font></font></strong></p>
<pre><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Input:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> nums = [1,1,1,2,2,3], k = 2
</font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Output:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> [1,2]
</font></font></pre><p><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Example 2:</font></font></strong></p>
<pre><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Input:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> nums = [1], k = 1
</font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Output:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> [1]
</font></font></pre>
<p>&nbsp;</p>
<p><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Constraints:</font></font></strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>k</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> is in the range </font></font><code>[1, the number of unique elements in the array]</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></li>
	<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">It is </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">guaranteed</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> that the answer is </font></font><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">unique</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">.</font></font></li>
</ul>

<p>&nbsp;</p>
<p><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Follow up:</font></font></strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> Your algorithm's time complexity must be better than </font></font><code>O(n log n)</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">, where n is the array's size.</font></font></p>
</div>