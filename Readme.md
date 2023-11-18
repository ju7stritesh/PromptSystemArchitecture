## Prompt Engineering

### Reference architecture for the emerging LLM app stack

Components of the stack

- Contextual data
- Prompt few shot examples
- Query
- Output

Here we focus on the open source architecture and local deployment of models along with examples

**Data preprocessing/embedding** - Data needs to be stored for retrieval and focus on the most relevant documents using LLMs
. The example we use here is a question answering application where teachers are able to create question papers and students are able to answer them
and a score is calculated for each answer based on semantic similarity. We use csv to store the data in the [qa_database.csv](qa_database.csv)
csv format. One can use local databased or cloud pipleines such as Databricks etc.  for data-loading and transformation solutions, depending on the scale.
Script [store_data.py](store_data.py) does that for us

**Embedding the data** - High-dimensional data is transformed into low-dimensional vectors using an approach known as embeddings, 
a kind of feature learning technique in machine learning, all while maintaining the pertinent information. Dimensionality reduction 
is a procedure that helps the data become simpler and easier for machine learning algorithms to process.
We use Sentence Transformers library to embed the answers and store them in two ways 
in a csv or using chromadb. Scripts [embed_answers_csv.py](embed_answers_csv.py) and [embed_answers_chromadb.py](embed_answers_chromadb.py)
does that for us. The embeddings are stored in a vector database for efficiently storing, comparing, and retrieving up to billions of embeddings (i.e., vectors).
One can use PineCone for the same which is one of the most popular ones.

**Prompt Construction** - Incorporating contextual data is becoming increasingly important
for product differentiation. Few shot prompts have become a very good way to include some prior information 
for better and accurate results compared to zero show prompts. A more advanced prompting strategies, including chain-of-thought, self-consistency, 
generated knowledge etc. are being developed by orchestration framework like Langchain.
Here even though our application itself does not use any prompt/contextual data the script [langchain_tool.py](langchain_tool.py)
provides an idea how to use them. A tool is created in langchain that searches for the current events using SERPAPI 
to get the right information and llm is used to answer the question using the same information.
Remember to execute the prompt we need to initialize an agent to execute the tool.

**Prompt Execution/Inference** - OpenAI is the most common and widely used LLM used currently. 
The in-context learning pattern is effective at solving hallucination and data-freshness problems, in order to better support content-generation tasks.
Here we provide example of an open source LLM using FLAN-T5 model using [flan_llm.py](flan_llm.py).
Facebook's llama models are probably the best which are fine-tuned to create better models like Mistral AI etc.
The question answered by the llm "Please answer the question: Can humans achieve world peace and why? Give the rationale before answering."
Answer - World peace is the goal of humanity. Humans are not able to achieve world peace because they are not able to control their own actions. So the final answer is no.
I tried plugging this model with langchain agent replacing OpenAI but the support is not there yet.

**Agents** give AI apps a fundamentally new set of capabilities: to solve complex problems, to act on the outside world, and to learn from experience post-deployment, solving hallucination and data-freshness problems. 
They do this through a combination of advanced reasoning/planning, tool usage, and memory / recursion / self-reflection.

Let's get back to the application and generate a score for the questions answered where many techniques could be used like weighted scores from each embedding depending on the accuracy levels. 
Cleaning the answers to focus mostly on important words before comparison etc. 
I have not done any of that in this example but may due so in the future. The goal 
is to provide an overview of prompt engineering in a simple manner.

## My thoughts:
The orchestration framework is still at its infancy with agents not really working as expected and developers are still trying to figure out 
how to utilize them effectively. Contextual data will become more and more important and
increasing the context window size will be a focus for most. Data pipelines still
don't fully cater to the challenges such as efficient data transformation or loading
and varies across developers. Fine-tuned models are becoming more important when focussing on 
specific use cases.

**Final thought** - In the realm of business, prompt engineering serves as a strategic lever, 
fine-tuning interactions to extract valuable insights, enhance decision-making, and propel an organization towards success.

