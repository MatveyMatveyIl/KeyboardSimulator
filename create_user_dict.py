import re
import dictionary


def multiple_replace(string_to_parse):
    replace_values = ['.', ',', '!', '?', ':', ';', '-']
    for i in replace_values:
        string_to_parse = string_to_parse.replace(i, '')
    return string_to_parse


def create_words(text):
    # dictionary.sentences[topic] = list(filter(lambda x: len(x) > 3,
    #                                           [x.strip() for x in multiple_replace(text).split(' ')]))
    return list(filter(lambda x: len(x) > 4,
                                              [x.strip() for x in multiple_replace(text).split(' ')]))


def create_sentences(text):
    return list(filter(lambda x: len(x) > 10,
                       [x.strip() for x in re.split('\.|\?|!|\n', text)]))


def create_text(text):
    return text

#s = [x for x in input().split('\n')]
a = set()
for i in open('text.txt'):
    if len(i) > 4:
        a.add(i.split('\n')[0])
a = list(a)
print(a)
a = "['particular', 'civil', 'term', 'sing', 'reason', 'individual', 'recently', 'another', 'occur', 'national', 'shot', 'look', 'others', 'situation', 'enter', 'attack', 'often', 'drive', 'carry', 'ahead', 'book', 'less', 'charge', 'shoot', 'majority', 'enough', 'particularly', 'whole', 'four', 'local', 'always', 'mouth', 'smile', 'their', 'industry', 'which', 'everyone', 'mission', 'scene', 'institution', 'sign', 'seek', 'degree', 'table', 'wrong', 'relationship', 'establish', 'herself', 'claim', 'contain', 'life', 'election', 'away', 'scientist', 'stage', 'response', 'fall', 'worker', 'debate', 'blood', 'fear', 'outside', 'according', 'everybody', 'despite', 'rise', 'western', 'problem', 'assume', 'thought', 'thank', 'ground', 'remain', 'head', 'writer', 'point', 'member', 'sometimes', 'speak', 'walk', 'visit', 'weight', 'believe', 'spend', 'actually', 'economic', 'network', 'large', 'fish', 'range', 'dream', 'short', 'small', 'will', 'here', 'reflect', 'myself', 'think', 'hundred', 'middle', 'serious', 'deal', 'trial', 'benefit', 'author', 'perform', 'plan', 'style', 'name', 'wind', 'final', 'raise', 'suffer', 'break', 'challenge', 'budget', 'clear', 'forget', 'piece', 'place', 'seem', 'among', 'Congress', 'where', 'anything', 'single', 'death', 'same', 'face', 'line', 'maintain', 'process', 'computer', 'tonight', 'fine', 'product', 'politics', 'leave', 'night', 'happy', 'executive', 'step', 'just', 'health', 'green', 'north', 'real', 'rock', 'chance', 'whom', 'yourself', 'whatever', 'business', 'possible', 'even', 'travel', 'food', 'idea', 'study', 'crime', 'machine', 'husband', 'property', 'task', 'good', 'floor', 'paper', 'base', 'difference', 'dinner', 'improve', 'rich', 'fund', 'road', 'experience', 'brother', 'across', 'reach', 'increase', 'adult', 'drug', 'pain', 'employee', 'much', 'work', 'recognize', 'support', 'many', 'such', 'family', 'kitchen', 'common', 'notice', 'society', 'major', 'impact', 'mind', 'land', 'most', 'defense', 'meet', 'school', 'teacher', 'back', 'growth', 'thing', 'eight', 'note', 'positive', 'three', 'administration', 'religious', 'since', 'love', 'other', 'summer', 'side', 'drop', 'toward', 'disease', 'thousand', 'available', 'baby', 'read', 'feel', 'avoid', 'into', 'probably', 'general', 'project', 'radio', 'although', 'call', 'instead', 'list', 'newspaper', 'agency', 'free', 'city', 'know', 'moment', 'still', 'evening', 'east', 'child', 'only', 'pull', 'amount', 'those', 'camera', 'hope', 'human', 'investment', 'tough', 'keep', 'than', 'movement', 'third', 'prepare', 'your', 'heavy', 'usually', 'tree', 'behavior', 'cover', 'second', 'community', 'case', 'fight', 'mother', 'speech', 'ever', 'white', 'structure', 'reduce', 'miss', 'that', 'decade', 'knowledge', 'like', 'about', 'cause', 'explain', 'certainly', 'important', 'relate', 'cell', 'difficult', 'foot', 'everything', 'price', 'laugh', 'personal', 'subject', 'exist', 'blue', 'ready', 'respond', 'information', 'near', 'live', 'allow', 'stay', 'church', 'understand', 'company', 'magazine', 'system', 'clearly', 'check', 'news', 'word', 'story', 'fail', 'share', 'heat', 'total', 'until', 'through', 'trip', 'chair', 'agree', 'seven', 'quality', 'skin', 'sell', 'director', 'course', 'finally', 'indeed', 'value', 'private', 'strategy', 'from', 'federal', 'pressure', 'market', 'marriage', 'area', 'must', 'never', 'change', 'write', 'future', 'question', 'father', 'operation', 'result', 'answer', 'truth', 'field', 'wife', 'rest', 'easy', 'television', 'find', 'great', 'money', 'official', 'various', 'morning', 'resource', 'spring', 'else', 'safe', 'central', 'again', 'describe', 'number', 'vote', 'high', 'former', 'friend', 'consider', 'first', 'seat', 'admit', 'economy', 'home', 'continue', 'cost', 'shake', 'minute', 'responsibility', 'treat', 'management', 'simple', 'quickly', 'career', 'quite', 'option', 'analysis', 'material', 'image', 'woman', 'realize', 'traditional', 'best', 'however', 'board', 'nearly', 'along', 'very', 'offer', 'someone', 'staff', 'film', 'fact', 'kind', 'million', 'rate', 'reality', 'town', 'right', 'whose', 'professional', 'against', 'memory', 'American', 'lead', 'week', 'hang', 'interview', 'success', 'song', 'close', 'compare', 'main', 'movie', 'office', 'college', 'democratic', 'include', 'attorney', 'class', 'record', 'provide', 'there', 'nothing', 'agreement', 'himself', 'stand', 'yard', 'entire', 'officer', 'player', 'join', 'left', 'environmental', 'last', 'service', 'appear', 'person', 'education', 'either', 'court', 'choice', 'should', 'together', 'enjoy', 'type', 'stop', 'surface', 'more', 'apply', 'perhaps', 'well', 'world', 'down', 'play', 'simply', 'Democrat', 'energy', 'expert', 'legal', 'pattern', 'involve', 'exactly', 'month', 'send', 'beat', 'yeah', 'behind', 'interest', 'south', 'bring', 'threat', 'choose', 'create', 'none', 'item', 'throw', 'sort', 'approach', 'size', 'suddenly', 'start', 'season', 'country', 'born', 'series', 'interesting', 'billion', 'power', 'before', 'build', 'issue', 'report', 'poor', 'lawyer', 'once', 'whether', 'page', 'team', 'loss', 'attention', 'Republican', 'push', 'method', 'race', 'inside', 'likely', 'security', 'them', 'training', 'room', 'ability', 'policy', 'bank', 'past', 'upon', 'able', 'couple', 'onto', 'could', 'measure', 'each', 'group', 'treatment', 'begin', 'design', 'force', 'discuss', 'want', 'almost', 'military', 'color', 'sound', 'audience', 'help', 'time', 'then', 'special', 'shoulder', 'different', 'practice', 'have', 'tend', 'grow', 'wear', 'tell', 'somebody', 'period', 'party', 'also', 'expect', 'next', 'identify', 'hear', 'animal', 'character', 'collection', 'window', 'give', 'fast', 'patient', 'become', 'fill', 'effort', 'listen', 'consumer', 'order', 'learn', 'young', 'hard', 'candidate', 'people', 'article', 'professor', 'talk', 'late', 'every', 'require', 'population', 'space', 'wish', 'prove', 'building', 'evidence', 'what', 'discover', 'reveal', 'indicate', 'forward', 'girl', 'medical', 'black', 'especially', 'political', 'because', 'social', 'media', 'west', 'leader', 'huge', 'nation', 'better', 'between', 'section', 'determine', 'accept', 'partner', 'suggest', 'account', 'condition', 'science', 'come', 'return', 'conference', 'center', 'hand', 'remember', 'part', 'hair', 'sexual', 'cultural', 'discussion', 'lose', 'natural', 'public', 'daughter', 'move', 'produce', 'skill', 'president', 'take', 'teach', 'similar', 'body', 'catch', 'pretty', 'technology', 'long', 'trouble', 'owner', 'activity', 'though', 'southern', 'kill', 'draw', 'generation', 'hotel', 'goal', 'data', 'guess', 'garden', 'under', 'show', 'language', 'culture', 'music', 'victim', 'within', 'cold', 'figure', 'cancer', 'ball', 'stuff', 'year', 'imagine', 'beautiful', 'station', 'strong', 'after', 'front', 'customer', 'decide', 'finish', 'necessary', 'five', 'receive', 'region', 'soon', 'coach', 'stock', 'turn', 'manager', 'argue', 'letter', 'today', 'wall', 'weapon', 'certain', 'little', 'with', 'above', 'present', 'beyond', 'might', 'these', 'star', 'sense', 'history', 'production', 'fire', 'bill', 'modern', 'action', 'care', 'meeting', 'sure', 'statement', 'decision', 'police', 'purpose', 'address', 'event', 'heart', 'something', 'direction', 'senior', 'source', 'picture', 'role', 'view', 'early', 'anyone', 'program', 'throughout', 'wide', 'some', 'detail', 'authority', 'form', 'sport', 'example', 'light', 'around', 'student', 'worry', 'would', 'open', 'level', 'both', 'control', 'represent', 'commercial', 'itself', 'century', 'development', 'painting', 'edge', 'glass', 'popular', 'environment', 'plant', 'hour', 'participant', 'recent', 'score', 'factor', 'citizen', 'maybe', 'card', 'full', 'message', 'street', 'feeling', 'alone', 'when', 'doctor', 'during', 'focus', 'really', 'nice', 'research', 'risk', 'opportunity', 'this', 'half', 'true', 'develop', 'concern', 'foreign', 'remove', 'follow', 'deep', 'test', 'make', 'position', 'themselves', 'without', 'mention', 'thus', 'effect', 'matter', 'while', 'hospital', 'manage', 'violence', 'finger', 'several', 'they', 'state', 'door', 'successful', 'agent', 'standard', 'save', 'serve', 'prevent', 'happen', 'phone', 'store', 'dark', 'nature', 'sister', 'capital', 'unit', 'watch', 'soldier', 'voice', 'government', 'model', 'pass', 'including', 'game', 'campaign', 'current', 'parent', 'wait', 'hold', 'later', 'wonder', 'affect', 'peace', 'house', 'significant', 'organization', 'performance', 'international', 'specific', 'pick', 'financial', 'rule', 'dead', 'protect', 'least', 'rather', 'site', 'over', 'need', 'theory', 'artist', 'arrive', 'water', 'physical', 'firm', 'mean', 'already', 'trade']"
for i in a.split(','):
    print(i)

