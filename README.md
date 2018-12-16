# CoderChef Kitchen :cake: :lollipop::icecream::doughnut:

The aim of CoderChef Kitchen is to be a one-stop shop for programmers, both experienced and amateurs alike to brush up and hone their programming skills. The repository contains well documented mini-blogs for a vast variety of programming problems.

* :fire: Programming problems from some of the best online judges like [Leetcode.com](https://leetcode.com), [Codechef.com](http://codechef.com) etc.
* :tada: Each problem has an intuition section, followed by the algorithm and the pseudo-code, and finally the implementation. Additionally, the problems are embellished with explanatory images and animations to provide clarity of thought.
* :pencil2: For now, we only add solutions in Python for the questions. Contributions are always welcome for solutions in other programming languages.

### Contribution Guideline

1. Clone the repo using the command
    ```
    git clone https://github.com/DivyaGodayal/CoderChef-Kitchen.git
    ```
2. For every problem, we expect you to create a separate folder in the respective section. For e.g. if you are solve a problem on LeetCode related to Dynamic Programming, then create a folder in the problem under the Dynamic Programming folder.

    ```
    mkdir Dynamic-Programming/<Problem Name>
    ```

3. The newly created folder must contain a `README.md` file and `solution.py` file. If there are multiple solutions, you can name the solutions accordingly. e.g. `solution_min_heap.py` or `solution_recursive.py`.

    ```
    touch README.md
    touch solution.py
    ```
4. For writing the README.md file, follow the template provided [Here](template.md)
5. Ideally, every approach to a programming problem should have the following sections:
      1. Motivation.
      2. Algorithm.
      3. Implementation Details. (Optional)
      4. Complexity Analysis.
6. Once all your changes are done, create a local commit.

    ```
    git add .
    git commit -am "Added article and solution for <Problem-Name>"
    ```
7. Push your changes to a separate branch for the problem. This new branch should be deleted once the PR is merged.

    ```
    git push origin master:<branch_name>
    ```
8. Raise a Pull Request. For further reading on how to raise a PR, read [this.](https://help.github.com/articles/creating-a-pull-request/)    

|    | Problem                             | Platform | Link                                                                                                                       |
|----|-------------------------------------|----------|----------------------------------------------------------------------------------------------------------------------------|
| 1  | Daily-Temperatues                   | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Daily-Temperatues)                              |
| 2  | Fake-Binary-Search                  | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Fake-Binary-Search)                             |
| 3  | Fizz-Buzz                           | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Fizz-Buzz)                                      |
| 4  | Hand-of-Straights                   | CodeChef | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Hand-of-Straights)                              |
| 5  | Implement-Magic-Dictionary          | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Implement-Magic-Dictionary)                     |
| 6  | Integer-to-English-Words            | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Integer-to-English-Words)                       |
| 7  | Lemonade-Change                     | CodeChef | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Lemonade-Change)                                |
| 8  | Min-Rotated-Sorted-Array            | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Min-Rotated-Sorted-Array)                       |
| 9  | Minimum-Refueling-Stops             | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Minimum-Refueling-Stops)                        |
| 10 | Score-After-Flipping-Matrix         | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Score-After-Flipping-Matrix)                    |
| 11 | Score-of-Parentheses                | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Score-of-Parentheses)                           |
| 12 | Set-Matrix-Zeros                    | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Set-Matrix-Zeros)                               |
| 13 | Spiral-Matrix                       | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Spiral-Matrix)                                  |
| 14 | Split-Array-into-Fibonacci-Sequence | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Split-Array-into-Fibonacci-Sequence)            |
| 15 | Task-Scheduler                      | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Adhoc/Task-Scheduler)                                 |
| 16 | 2-Keys                              | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/2-Keys)                           |
| 17 | 4-Keys                              | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/4-Keys)                           |
| 18 | Change-the-Signs                    | CodeChef | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/Change-the-Signs)                 |
| 19 | Matchsticks-to-Square               | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/Matchsticks-to-Square)            |
| 20 | Soup-Servings                       | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Dynamic-Programming/Soup-Servings)                    |
| 21 | All-Nodes-Distance-K-in-Binary-Tree | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/All-Nodes-Distance-K-in-Binary-Tree) |
| 22 | Bus-Routes                          | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Bus-Routes)                          |
| 23 | Cheapest-Flight-Within-K-Stops      | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Cheapest-Flight-Within-K-Stops)      |
| 24 | Cracking-the-Safe                   | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Cracking-the-Safe)                   |
| 25 | Evaluate-Division                   | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Evaluate-Division)                   |
| 26 | Flatten-Binary-Tree                 | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Flatten-Binary-Tree)                 |
| 27 | Making-A-Large-Island               | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Making-A-Large-Island)               |
| 28 | Path-Sum                            | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Path-Sum)                            |
| 29 | Remove-Invalid-Parenthesis          | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Remove-Invalid-Parenthesis)          |
| 30 | Sum-of-Distances-In-a-Tree          | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Sum-of-Distances-In-a-Tree)          |
| 31 | Word-Search                         | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Graphs-And-Trees/Word-Search)                         |
| 32 | DeepCopy                            | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Linked-List/DeepCopy-LinkedList)                      |
| 33 | Isomorphic-Strings                  | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Strings/Isomorphic-Strings)                           |
| 34 | Minimum-Window-Substring            | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Strings/Minimum-Window-Substring)                     |
| 35 | Partition-Labels                    | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Strings/Partition-Labels)                             |
| 36 | Reorganize_String                   | LeetCode | [Link](https://github.com/DivyaGodayal/CoderChef-Kitchen/tree/master/Strings/Reorganize_String)                            |
