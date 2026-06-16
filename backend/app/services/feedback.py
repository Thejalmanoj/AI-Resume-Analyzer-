from typing import Any, List, Optional
from langchain_core.language_models.llms import LLM
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from langchain_core.prompts import PromptTemplate

class FlanT5LLM(LLM):
    model: Any = None
    tokenizer: Any = None

    def __init__(self, model_name="google/flan-t5-small"):
        super().__init__()
        object.__setattr__(self, "model", AutoModelForSeq2SeqLM.from_pretrained(model_name))
        object.__setattr__(self, "tokenizer", AutoTokenizer.from_pretrained(model_name))

    @property
    def _llm_type(self) -> str:
        return "flan-t5"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=512)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

llm = FlanT5LLM()



template="""

Analyze this resume.

Resume:
{resume}

Job Description:
{jd}

Give:

1. ATS weaknesses

2. Missing skills

3. Resume improvements

4. Suggested projects

5. Hiring probability
"""


prompt=PromptTemplate(

input_variables=[
    "resume",
    "jd"
],

template=template
)


def generate_feedback(
resume,
jd
):

    chain=prompt|llm

    result=chain.invoke(

        {
            "resume":resume[:1500],
            "jd":jd[:1000]
        }

    )

    # HuggingFacePipeline returns a string directly
    return result