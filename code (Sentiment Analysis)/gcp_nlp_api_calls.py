from google.cloud import language_v1

client = language_v1.LanguageServiceClient.from_service_account_json("**********.json")
def get_res(x):
    text_content = x.review
    rest_name=x.restaurant_name
    encoding_type = language_v1.EncodingType.UTF8
    type_ = language_v1.types.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}
    response = client.analyze_entity_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    df = pd.DataFrame(columns=['restaurant_name','review','entity_name','entity_sentiment_score'])
    for entity in response.entities:
        df1 = pd.DataFrame(columns=['restaurant_name','review','entity_name','entity_sentiment_score'])
        df1.columns = ['restaurant_name','review','entity_name','entity_sentiment_score']
        df1['restaurant_name'] = [rest_name]
        df1['review'] = [text_content]
        df1['entity_name'] = [entity.name]
        df1['entity_sentiment_score'] = [entity.sentiment.score]
        df=pd.concat([df, df1], axis=0)  
    return df
