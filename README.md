# hello-world
Learning github with official documentation

## Copy Permanentlink

https://github.com/Raju-Praveen/WhatsApp-Clone/blob/b0559e420eac47748bfb1735abb7cee6ac0cae12/home_screen.py?plain=1#L30C1-L37

## Mathematical expression

Expression: $\sqrt{2x+1}+(1+x)^6$

## **Cauchy-Schwarz inequality**

```math
\left( \sum_{i=1}^n a_k b_k\right)^2 \leq \left( \sum_{i=1}^n a_k^2 \right) \left( \sum_{i=1}^n b_k^2 \right)
```

```math
\sqrt{4}
```


### Simple flow chart:

## Mermaid node with text
```mermaid
flowchart LR
  id[Text in box]
  id1(Text with corner radius)
  id2([Elliptical box with text])
  id3[(Database diagram)]
  id4[[Rectangle with bonus]]
  id5((Text in circle))
  id6>Badge text with box]
  id7{Rhombus box}
  id7{{Hexagon box}}
  id8[/Right Parallelogram/]
  id9[\Left Parallelogram\]
  id10(((Double circle text)))
```

## Mermaid git graph

```mermaid
gitGraph
  commit
  commit
  commit
  branch develop
  checkout develop
  commit
  commit id: "Commit 5 now" type: REVERSE
  commit
  branch subbranch
  checkout subbranch
  commit type: HIGHLIGHT tag: "v2.0.5"
  commit
  checkout develop
  merge subbranch
  commit
  checkout main
  merge develop
  commit
  commit
```

```mermaid
gitGraph
  commit
  commit
  commit
  branch develop
  checkout develop
  commit
  commit id: "Commit 5 now" type: REVERSE
  commit id:"A"
  branch subbranch
  checkout subbranch
  commit type: HIGHLIGHT tag: "v2.0.5"
  commit
  checkout develop
  merge subbranch
  commit
  checkout main
  cherry-pick id:"A"
  commit
  merge develop
```

## Mermaid Gantt diagram

```mermaid
gantt
dateFormat DD-MM-YYYY
title Adding Gantt to mermaid
excludes weekdays 2023-08-25

section A section
Task 1     :done, des1, 21-08-2023,23-08-2023
Task 2     :active, des2, 22-08-2023, 2d
Task 3     :       des3, 25-08-2023, 5d
Task 4     :       des4, 23-08-2023, 2d
```

## Mermaid Sequence diagram

```mermaid
sequenceDiagram
  participant Ace
  participant Diamond
  participant Heart
  participant Clever
  Ace->>Clever: How are you,Clever?
  Clever->>Diamond: Are you free?
  Clever-->>Ace: I'm fine. You?
  Diamond->>Heart: What is the project status?
  loop Project
    Heart->>Heart: Quickly solve the issue 28
  end
  Diamond-->>Clever: No, I'm working now.
  Ace->>Clever: Fine. Thank you!
  Heart-->>Diamond: Completed, Diamond.
  Note right of Ace: Simple note for Ace
```


# Changes
## This is the first change
This is done for learning in creating new branch named readme-edits.
[hello](https://google.com)
1. one
2. two
3. three

-    un
-    order
-    list

> Code
[Contribution](./contribute.md)

<picture>
  <img alt="(prefer-color-scheme: dark)" src="./image1.jpg">
</picture>

|Rank|Languages|
|---:|---:|
|1.| Python|
|3.|Java|
|2.|Django|
|4.|Flask|


Footer 1[^1]
Footer multi line [^2]

[^1]: Footer content 1.
[^2]: Footer content with 2 spaces.
  multiple line.

> [!NOTE]
> This is a note sentence.

> [!IMPORTANT]
> This is a important sentence.

> [!WARNING]
> This is a warning sentence.

|Command|Description|
|:---:|:----|
|`re.compile`|It's a regular expression for python|
|`sys.argv`|It gets a command line argument as input in main method|
|`numpy.array`|Numpy array for multi-dimensional array processing|

<details>
<summary>This is a summary for dropdown menu</summary>
  
## Heading 2
````java
  class Main{
    public static void main(String[] args){
      Main main = new Main();
      System.out.println("Hello World");
      main.showName();
    }

    void showName(){
      System.out.println("This is GitHub");
    }
  }
````
</details>

