from .preprocessor_base import PreprocessorBase


class Preprocessor(PreprocessorBase):

    def _transform_document(self, doc):
        contents = "\n".join([doc["title"], doc["description"]]
                             + list(doc["data_fields"].values()))
        newdoc = dict(
            id=doc['id'],
            contents=contents
        )
        return newdoc
