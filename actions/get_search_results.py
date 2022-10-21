from googlesearch import *
from googlesearch.exceptions import RelatedSearchError
from st2common.runners.base_action import Action


class GetSearchResultsAction(Action):
    def run(self, query, count=10):
        srch = Search(query.lower(), number_of_results=count)
        srch.load()
        return (True, {"result": srch.as_dict()})
