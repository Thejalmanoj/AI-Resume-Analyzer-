from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model=SentenceTransformer(
    'all-MiniLM-L6-v2'
)

def get_embedding(text):

    vector=model.encode([text])

    return np.array(
        vector
    ).astype("float32")


def semantic_similarity(
    resume,
    jd
):

    resume_vector=get_embedding(
        resume
    )

    jd_vector=get_embedding(
        jd
    )

    dimension=resume_vector.shape[1]

    index=faiss.IndexFlatL2(
        dimension
    )

    index.add(
        jd_vector
    )

    D,I=index.search(
        resume_vector,
        1
    )

    similarity=1/(1+float(D[0][0]))

    return float(round(
        similarity*100,
        2
    ))