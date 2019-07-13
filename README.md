# CoderChef Kitchen :cake: :lollipop::icecream::doughnut:

The aim of CoderChef Kitchen is to be a one-stop shop for programmers, both experienced and amateurs alike to brush up and hone their programming skills. The repository contains well documented mini-blogs for a vast variety of programming problems.

* :fire: Programming problems from some of the best online judges like [Leetcode.com](https://leetcode.com), [Codechef.com](http://codechef.com) etc.
* :tada: Each problem has an intuition section, followed by the algorithm and the pseudo-code, and finally the implementation. Additionally, the problems are embellished with explanatory images and animations to provide clarity of thought.
* :pencil2: For now, we only add solutions in Python for the questions. Contributions are always welcome for solutions in other programming languages.

## How to Contribute ?

When people start off with their programming journey, they usually come across algorithms like Linear Search, Bubble Sort, Insertion Sort and much more. There are a *bazillion* resources out there for such introductory algorithms.

Our aim with Code**r**Chef Kitchen (Don't miss that 'r' 😅) is not to add articles just for the sake of it. Our main intention is to add articles that bring across some important programming concepts or some new algorithmic techniques or some interesting implementation ideas that we don't generally find online.

In addition to this, we want to make programming fun for people out there. We want to break away from the common notion of *"tech articles are boring and serious"*. They can be pretty fun and addictive to read, if projected in a certain way.

<p align="center">
<img src="Images/snoopy-readme.gif" width="600">
</p>

There are multiple ways in which you can contribute. There are no "prerequisites" as such for you to become a contributor. Essentially, you can do either of the following:

1. Pick up one of the existing problems from the repository and add a solution in a language not already present in the repo. For e.g. a lot of problems currently only have solutions in Python. It would be great to have solutions in other common languages like Java or C/C++.

    An important thing to consider here is that the solution you provide must be ***in line*** with the algorithm(s) already explained in the article. In case you are writing a new algorithm which has not been explained already, then make sure to add relevant explanation to the article as well.

2. The second way for you to contribute is by picking a problem which is not already there in the repository and contribute solution(s) and an article for it.

    > A picture is worth a thousand words

    That is our motto. The articles that we write tend to be full of illustrations in the form of explanatory diagrams and gifs/videos/animations. Anything that helps explain the algorithm better. We would love future articles to be along the same lines as well. For a detailed set of guidelines for contributing a new article, read the instructions below.

    <p align="center">
    <img src="Images/motto.gif" width="600">
    </p>

### Contribution Guideline

1. The first thing you should do is, convey what you want to contribute. To make it a very streamlined process, create an **issue** in the repository describing the problem you want to pick. Also, in 1-2 lines explain why you think this problem should be added to the repo.

    **Kindly note** this step is only to be sure that your efforts won't go to waste. Once the issue is approved, you can go ahead with article. This still doesn't guarantee that your article would be accepted on the first go. Our only suggestion is stick to the template (read below) and be as creative as possible. We are always there to help and learn in the process.

2. Clone the repo using the command
    ```
    git clone https://github.com/DivyaGodayal/CoderChef-Kitchen.git
    ```
3. For every **new** problem, create a separate folder in the respective section. For e.g. if you are solving a problem on LeetCode related to Dynamic Programming, create a folder for the problem under the Dynamic Programming folder.

    ```
    mkdir Dynamic-Programming/<Problem Name>
    ```

4. The newly created folder must contain a `README.md` file and `solution.py` file. If there are multiple solutions, you can name the solutions accordingly. e.g. `solution_min_heap.py` or `solution_recursive.py`.

    ```
    touch README.md
    touch solution.py
    ```
5. For writing the README.md file, follow the template provided [here](Template/README.md).
6. Ideally, every approach to a programming problem should have the following sections:
      1. Motivation.
      2. Algorithm.
      3. Implementation Details. (Optional)
      4. Complexity Analysis.
7. Once you are done writing the article and the solutions, remember to add the problem to the table on the main README page. (Look at the table of contents below).  
8. Once all your changes are done, create a local commit.

    ```
    git add .
    git commit -am "Added article and solution for <Problem-Name>"
    ```
9. Push your changes to a separate branch for the problem. This new branch should be deleted once the PR is merged.

    ```
    git push origin master:<branch_name>
    ```
10. Raise a Pull Request. This step is very important. For any changes you want to make to the repository, you have to raise a pull request. For further reading on how to raise a PR, read [this.](https://help.github.com/articles/creating-a-pull-request/)    
11. In case of any doubt in the above steps, reach out to us. :)

<table>
  <tr>
    <th colspan="4"><h3>Adhoc Problems</h3></th>
  </tr>
  <tr>
    <td></td>
    <td><b>Problem</b></td>
    <td><b>Platform</b></td>
    <td><b>Link</b></td>
  </tr>
  <tr>
    <td>1</td>
    <td>Daily Temperatues</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Daily-Temperatues">Link</a></td>
  </tr>
  <tr>
    <td>2</td>
    <td>Fake Binary Search</td>
    <td>CodeChef</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Fake-Binary-Search">Link</a></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Fizz Buzz</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Fizz-Buzz">Link</a></td>
  </tr>
  <tr>
    <td>4</td>
    <td>Hand of Straights</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Hand-of-Straights">Link</a></td>
  </tr>
  <tr>
    <td>5</td>
    <td>Implement Magic Dictionary</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Implement-Magic-Dictionary">Link</a></td>
  </tr>
  <tr>
    <td>6</td>
    <td>Integer to English-Words</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Integer-to-English-Words">Link</a></td>
  </tr>
  <tr>
    <td>7</td>
    <td>Lemonade Change</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Lemonade-Change">Link</a></td>
  </tr>
  <tr>
    <td>8</td>
    <td>Minimum in Rotated Sorted Array</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Min-Rotated-Sorted-Array">Link</a></td>
  </tr>
  <tr>
    <td>9</td>
    <td>Minimum Refueling Stops</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Minimum-Refueling-Stops">Link</a></td>
  </tr>
  <tr>
    <td>10</td>
    <td>Score After Flipping Matrix</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Score-After-Flipping-Matrix">Link</a></td>
  </tr>
  <tr>
    <td>11</td>
    <td>Score of Parentheses</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Score-of-Parentheses">Link</a></td>
  </tr>
  <tr>
    <td>12</td>
    <td>Set Matrix Zeros</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Set-Matrix-Zeros">Link</a></td>
  </tr>
  <tr>
    <td>13</td>
    <td>Spiral Matrix</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Spiral-Matrix">Link</a></td>
  </tr>
  <tr>
    <td>14</td>
    <td>Split Array into Fibonacci Sequence</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Split-Array-into-Fibonacci-Sequence">Link</a></td>
  </tr>
  <tr>
    <td>15</td>
    <td>Task Scheduler</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Task-Scheduler">Link</a></td>
  </tr>
  <tr>
    <td>16</td>
    <td>2 Sum</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/N-Sum-Problems/2Sum">Link</a></td>
  </tr>
  <tr>
    <td>17</td>
    <td>3 Sum</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/N-Sum-Problems/3Sum">Link</a></td>
  </tr>
  <tr>
    <td>18</td>
    <td>4 Sum</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/N-Sum-Problems/4Sum">Link</a></td>
  </tr>
  <tr>
    <td>19</td>
    <td>Advantage Shuffle</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Advantage-Shuffle">Link</a></td>
  </tr>
  <tr>
    <td>20</td>
    <td>Next Greater Element I</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Next-Greater-Element-I">Link</a></td>
  </tr>
  <tr>
    <td>21</td>
    <td>Next Greater Element II</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Next-Greater-Element-II">Link</a></td>
  </tr>
    <tr>
    <td>22</td>
    <td>Rotate Array</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Rotate-Array">Link</a></td>
  </tr>
  <tr>
    <td>23</td>
    <td>Maximum Product of Word Lengths</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Maximum-Product-of-Word-Lengths">Link</a></td>
  </tr>
  <tr>
    <td>24</td>
    <td>Asteroid Collision</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Asteroid-Collision">Link</a></td>
  </tr>
  <tr>
    <td>25</td>
    <td>Generate Parantheses</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Generate-Parentheses">Link</a></td>
  </tr>
  <tr>
    <td>26</td>
    <td>Top K Frequent Words</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Top-K-Frequent-Words">Link</a></td>
  </tr>
  <tr>
    <th colspan="4"><h3>Dynamic Programming</h3></th>
  </tr>
  <tr>
    <td>1</td>
    <td>2-Keys</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/2-Keys">Link</a></td>
  </tr>
  <tr>
    <td>2</td>
    <td>4-Keys</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/4-Keys">Link</a></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Change the Signs</td>
    <td>CodeChef</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/Change-the-Signs">Link</a></td>
  </tr>
  <tr>
    <td>4</td>
    <td>Matchsticks to Square</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/Matchsticks-to-Square">Link</a></td>
  </tr>
  <tr>
    <td>5</td>
    <td>Soup Servings</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/Soup-Servings">Link</a></td>
  </tr>
  <tr>
    <td>6</td>
    <td>Optimal Division</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/Optimal-Division">Link</a></td>
  </tr>
  <tr>
    <td>7</td>
    <td>Largest Sum of Averages</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/Largest-Sum-of-Averages">Link</a></td>
  </tr>
  <tr>
    <td>8</td>
    <td>Climbing Stairs</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/Climbing-Stairs">Link</a></td>
  </tr>
  <tr>
    <td>9</td>
    <td>Video Stitching</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/Video-Stitching">Link</a></td>
  </tr>
  <tr>
    <th colspan="4"><h3>Graphs and Trees</h3></th>
  </tr>
  <tr>
    <td>1</td>
    <td>All Nodes Distance K in Binary Tree</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/All-Nodes-Distance-K-in-Binary-Tree">Link</a></td>
  </tr>
  <tr>
    <td>2</td>
    <td>Bus Routes</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Bus-Routes">Link</a></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Cheapest Flight Within K Stops</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Cheapest-Flight-Within-K-Stops">Link</a></td>
  </tr>
  <tr>
    <td>4</td>
    <td>Cracking the Safe</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Cracking-the-Safe">Link</a></td>
  </tr>
  <tr>
    <td>5</td>
    <td>Evaluate Division</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Evaluate-Division">Link</a></td>
  </tr>
  <tr>
    <td>6</td>
    <td>Flatten Binary Tree</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Flatten-Binary-Tree">Link</a></td>
  </tr>
  <tr>
    <td>7</td>
    <td>Making A Large Island</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Making-A-Large-Island">Link</a></td>
  </tr>
  <tr>
    <td>8</td>
    <td>Path Sum</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Path-Sum">Link</a></td>
  </tr>
  <tr>
    <td>9</td>
    <td>Remove Invalid Parenthesis</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Remove-Invalid-Parenthesis">Link</a></td>
  </tr>
  <tr>
    <td>10</td>
    <td>Sum of Distances In a Tree</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Sum-of-Distances-In-a-Tree">Link</a></td>
  </tr>
  <tr>
    <td>11</td>
    <td>Word Search</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Word-Search">Link</a></td>
  </tr>
  <tr>
    <td>12</td>
    <td>Number of Islands</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Number-of-Islands">Link</a></td>
  </tr>
  <tr>
    <td>13</td>
    <td>Largest-Value in Each Tree Row</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Largest-Value-in-Each-Tree-Row">Link</a></td>
  </tr>
  <tr>
    <td>14</td>
    <td>Construct a Binary Tree from in-order and Postorder Traversal</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Binary-Tree-from-Inorder-and-Postorder-Traversal">Link</a></td>  
  </tr>
  <tr>
    <td>15</td>
    <td>Add One Row to Tree</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Add-One-Row-to-Tree">Link</a></td>  
  </tr>
  <tr>
    <th colspan="4"><h3>Linked-List</h3></th>
  </tr>
  <tr>
    <td>1</td>
    <td>DeepCopy</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Linked-List/DeepCopy-LinkedList">Link</a></td>
  </tr>
  <tr>
    <td>2</td>
    <td>Remove N<sup>th</sup> Node from End of List</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Linked-List/Remove-N-From-End">Link</a></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Remove Duplicates from Sorted List I</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Linked-List/Remove-Dups-from-Sorted-List">Link</a></td>
  </tr>
  <tr>
    <td>4</td>
    <td>Remove Duplicates from Sorted List II</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Linked-List/Remove-Dups-from-Sorted-List-II">Link</a></td>
  </tr>
  <tr>
    <td>5</td>
    <td>Sort List</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Linked-List/Sort-List">Link</a></td>
  </tr>
  <tr>
    <td>6</td>
    <td>Swap Nodes in Pairs</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Linked-List/Swap-Nodes-in-Pairs">Link</a></td>
  </tr>
  <tr>
    <td>7</td>
    <td>Linked List Components</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Linked-List/Linked-List-Components">Link</a></td>
  </tr>
  <tr>
    <th colspan="4"><h3>Strings</h3></th>
  </tr>
  <tr>
    <td>1</td>
    <td>Isomorphic Strings</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Strings/Isomorphic-Strings">Link</a></td>
  </tr>
  <tr>
    <td>2</td>
    <td>Minimum Window Substring</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Strings/Minimum-Window-Substring">Link</a></td>
  </tr>
  <tr>
    <td>3</td>
    <td>Partition Labels</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Strings/Partition-Labels%E2%80%8B">Link</a></td>
  </tr>
  <tr>
    <td>4</td>
    <td>Reorganize String</td>
    <td>LeetCode</td>
    <td><a href="https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Strings/Reorganize_String">Link</a></td>
  </tr>
</table>
