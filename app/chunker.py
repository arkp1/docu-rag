from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(
    text
):
    
    splitter = (
        RecursiveCharacterTextSplitter(chunk_size=500, 
                                              chunk_overlap=100)
    )



    

    return splitter.split_text(text)

# text = """

# Wales is a major global legal tradition that has been adopted or adapted by numerous countries worldwide.

# """

# chunks = create(text)

# print(chunks)



# manual chunking approach:

# def create_chunks(
#     text,
#     chunk_size=500,
#     chunk_overlap=100
# ):

#     chunks = []

#     start = 0

#     while start < len(text):
        
#         end = start + chunk_size

#         chunks.append(text[start:end])


#         start += chunk_size - chunk_overlap

#     return chunks