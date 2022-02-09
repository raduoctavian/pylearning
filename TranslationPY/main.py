from azure.core.credentials import AzureKeyCredential
from azure.ai.translation.document import DocumentTranslationClient

endpoint = "https://TranslationPY.cognitiveservices.azure.com/"
credential = AzureKeyCredential("0c4fe47fd6cd4a78a00b90a3423ab2cb")
document_translation_client = DocumentTranslationClient(endpoint, credential)