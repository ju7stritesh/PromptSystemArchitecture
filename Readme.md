## Prompt Engineering

### Reference architecture for the emerging LLM app stack

Components of the stack

- Contextual data
- Prompt few shot examples
- Query
- Output

Here we focus on the open source architecture and local deployment of models along with examples

**Application** - A simple question answering demo
- Question Answer Database - [qa_database.csv](qa_database.csv)
- Embedding Answers
- Compare answers

**Data preprocessing/embedding** - Using LLMs, data must be saved for retrieval with an emphasis on the most pertinent documents. We utilize a question-answering application as an example, where students can respond to teacher-created question papers and scores are determined based on semantic similarity. The data is stored in the [qa_database.csv](qa_database.csv) csv format using csv. Depending on the scale, one can leverage cloud platforms like Databricks or local databases for data loading and transformation.
That is done for us by the script [store_data.py](store_data.py).

**Embedding the data** - High-dimensional data is transformed into low-dimensional vectors using an approach known as embeddings, 
a kind of feature learning technique in machine learning, all while maintaining the pertinent information. Dimensionality reduction 
is a procedure that helps the data become simpler and easier for machine learning algorithms to process.
We use Sentence Transformers library to embed the answers and store them in two ways 
in a csv or using chromadb. Scripts [embed_answers_csv.py](embed_answers_csv.py) and [embed_answers_chromadb.py](embed_answers_chromadb.py)
does that for us. The embeddings are stored in a vector database for efficiently storing, comparing, and retrieving up to billions of embeddings (i.e., vectors).
One can use PineCone for the same which is one of the most popular ones.

**Prompt Construction** - Contextual data integration is becoming more and more crucial for product differentiation. 
When compared to zero show prompts, few shot prompts have shown to be an excellent method of including some prior 
information for more precise and superior results. More sophisticated prompting techniques, such as generated knowledge, self-consistency, and chain-of-thought, are being developed by orchestration frameworks like Langchain.
Here, the script [langchain_tool.py](langchain_tool.py) gives instructions on how to use prompts and contextual data, 
even though our application itself does not use any of them. A tool is developed in Langchain that uses SERPAPI to look up 
current events in order to obtain accurate information reducing hallucination. Then, using the same information, a llm is utilized to provide an answer to the query.
Don't forget to run the prompt. Before running the tool, an agent needs to be initialized (we talk about agents below).

**Prompt Execution/Inference** - Right now, OpenAI is the most popular and most utilized LLM. 
To enhance content-generation activities, the in-context learning pattern effectively addresses issues related to hallucinations and data freshness.
This is an example of an open-source LLM that uses the FLAN-T5 model, which can be found in [flan_llm.py](flan_llm.py).
The best llama models are probably those from Facebook, which are refined to produce better models like Mistral AI, among others.
The question answered by the llm "Please answer the question: Can humans achieve world peace and why? Give the rationale before answering."
Answer - World peace is the goal of humanity. Humans are not able to achieve world peace because they are not able to control their own actions. So the final answer is no.
I attempted to insert this model using the Langchain agent instead of OpenAI, but the support is not yet available.

**Agents** give AI apps a fundamentally new set of capabilities: to solve complex problems, to act on the outside world, and to learn from experience post-deployment, solving hallucination and data-freshness problems. 
They do this through a combination of advanced reasoning/planning, tool usage, and memory / recursion / self-reflection.

Let's get back to the application and generate a score for the questions answered where many techniques could be used like weighted scores from each embedding depending on the accuracy levels. 
Cleaning the answers to focus mostly on important words before comparison etc. 
I have not done any of that in this example but may due so in the future. The goal 
is to provide an overview of prompt engineering in a simple manner.

## My thoughts:
Since agents don't always function as planned and developers are still figuring out how to best use them, the orchestration framework is still in its infancy. 
The importance of contextual data will only grow, and most people's attention will be directed toward expanding the context window. 
Data pipelines still don't completely address issues like effective data loading and transformation, the use of which differs among engineers. 
The importance of refined models increases when concentrating on certain use cases.

## Real World Application - 
**Based on the concepts discussed above**,
I have developed a basic online application (from real user feedback) for answering questions that enables teachers to generate question papers and view the AI's feedback. Through the application, teachers and students have separate portals where students can complete question papers from various teachers and receive scores for both the overall and individual questions answered.
The data is preprocessed and postprocessed using sophisticated approaches (together with the marking system) to accommodate nearly every type of topic (philosophy, science, history, etc.), making the algorithm more sophisticated for the application.
There are still a lot of problems with score generation because the subject creates variants that need to be better managed and tailored to each unique use case.
Each of the three question categories in the application—MCQs, PointBased, and Subjective—has a unique method for producing a score.

### Screenshots for the same.
#### Teacher portal
![Tried7.png](WebApp%2FTried7.png)
#### Creating Tests
![Tried2.png](WebApp%2FTried2.png) 
#### Student's answer sheet
![Tried3.png](WebApp%2FTried3.png) 
#### Analyzing the AI score from the answer sheet
![Tried4.png](WebApp%2FTried4.png) 
#### Multi language support
![Tried6.png](WebApp%2FTried6.png)

**Final thought** - In the realm of business, prompt engineering serves as a strategic lever, 
fine-tuning interactions to extract valuable insights, enhance decision-making, and propel an organization towards success.

_**Note** : I have give a brief demonstration of the quick engineering chat generating application that includes context, 
covering the majority of the architecture's components here https://github.com/ju7stritesh/PromptEngineeringChatGeneration._
