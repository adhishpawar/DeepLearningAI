# LangChain Chains - README

## 1. What are Chains?

In **LangChain**, a **Chain** is a pipeline that connects multiple components together (Prompts, Models, Parsers, Tools, etc.) so that data flows automatically from one step to another.

Instead of calling each component separately, chains let you **orchestrate the entire flow** in a clean and modular way.

---

## 2. Why Chains are Needed?

* **Automation**: Connects steps automatically.
* **Reusability**: Easy to reuse in different workflows.
* **Flexibility**: Build pipelines with sequence, parallel, or conditional flows.
* **Traceability**: Easier to debug and visualize with graphs.

Example Flow (Prompt → LLM → OutputParser → Final Result):

```
+-----------------+       +-----------+       +-----------------+
|   PromptTemplate|  -->  |  ChatOpenAI|  --> | StrOutputParser |
+-----------------+       +-----------+       +-----------------+
```

---

## 3. Runnables in Chains

Behind the scenes, LangChain uses the concept of **Runnables**:

* Every component (`PromptTemplate`, `ChatOpenAI`, `StrOutputParser`) is a **Runnable**.
* You can connect them using the `|` operator.
* This makes it easy to build pipelines without writing boilerplate code.

---

## 4. Pipeline Flow Types

LangChain supports different types of pipelines:

1. **Simple (Linear)**: Step 1 → Step 2 → Step 3.
2. **Sequential**: Multiple steps executed in order.
3. **Parallel**: Multiple steps executed simultaneously.
4. **Conditional**: Execution depends on conditions.

---

## 5. Example Code

check simple_chain.py
---

---

## 6. Key Takeaways

* A **Chain** is simply a pipeline of `Runnables`.
* The `|` operator connects components together.
* The chain handles data flow automatically.
* `get_graph()` helps visualize the pipeline.

---

## 7. References

* [LangChain Docs - Chains](https://www.langchain.com/docs/expression_language/cookbook/chains)
* [LangChain Runnables](https://www.langchain.com/docs/expression_language/interface)
