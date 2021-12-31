import requests
from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.utils.asserts import assert_equal
from utils import utils


class requestsKeywords():

    def __init__(self):
        self.builtin = BuiltIn()
        self.timeout = None
        self.cookies = None
        self.last_response = None

    def _common_request(
            self,
            method,
            uri,
            **kwargs):

        method_function = getattr(requests, method)
        resp = method_function(
            uri,
            timeout=self._get_timeout(kwargs.pop('timeout', None)),
            cookies=kwargs.pop('cookies', self.cookies),
            **kwargs)

        self.last_response = resp

        return resp

    @staticmethod
    def _check_status(expected_status, resp, msg=None):
        """
        Method to check HTTP status
        """
        if expected_status is None:
            resp.raise_for_status()
        else:
            try:
                expected_status = int(expected_status)
            except ValueError:
                expected_status = utils.parse_named_status(expected_status)
            msg = '' if msg is None else '{} '.format(msg)
            msg = "{}Url: {} Expected status".format(msg, resp.url)
            assert_equal(resp.status_code, expected_status, msg)


    def _get_timeout(self, timeout):
        return float(timeout) if timeout is not None else self.timeout


    @keyword("Status Should Be")
    def status_should_be(self, expected_status, response=None, msg=None):
        if not response:
            response = self.last_response
        self._check_status(expected_status, response, msg)




    @keyword("GET")
    def session_less_get(self, url, params=None, **kwargs):
        """
        Sends a GET request.
        The endpoint used to retrieve the resource is the ``url``, while query
        string parameters can be passed as string, dictionary (or list of tuples or bytes)
        through the ``params``.
        Other optional requests arguments can be passed using ``**kwargs`` here is a list:
        | ``data``     | Dictionary, list of tuples, bytes, or file-like object to send in the body of the request. |
        | ``json``     | A JSON serializable Python object to send in the body of the request. |
        | ``headers``  | Dictionary of HTTP Headers to send with the request. |
        | ``cookies``  | Dict or CookieJar object to send with the request. |
        | ``files``    | Dictionary of file-like-objects (or ``{'name': file-tuple}``) for multipart encoding upload. |
        | ``file-tuple`` | can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')`` or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers to add for the file. |
        | ``auth`` | Auth tuple to enable Basic/Digest/Custom HTTP Auth. |
        | ``timeout`` | How many seconds to wait for the server to send data before giving up, as a float, or a ``(connect timeout, read timeout)`` tuple. |
        | ``allow_redirects`` | Boolean. Enable/disable GET/OPTIONS/POST/PUT/PATCH/DELETE/HEAD redirection. Defaults to ``True``. |
        | ``proxies`` | Dictionary mapping protocol or protocol and host to the URL of the proxy (e.g. {'http': 'foo.bar:3128', 'http://host.name': 'foo.bar:4012'}) |
        | ``verify``  | Either a boolean, in which case it controls whether we verify the server's TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to ``True``. Warning: if a session has been created with ``verify=False`` any other requests will not verify the SSL certificate. |
        | ``stream`` | if ``False``, the response content will be immediately downloaded. |
        | ``cert`` | if String, path to ssl client cert file (.pem). If Tuple, ('cert', 'key') pair. |
        """
        response = self._common_request('get',url,
                                        params=params, **kwargs)
        return response

    @keyword('POST')
    def session_less_post(self, url, data=None, json=None, **kwargs):
        """
        Sends a POST request.
        The endpoint used to send the request is the ``url`` parameter, while its body
        can be passed using ``data`` or ``json`` parameters.
        ``data`` can be a dictionary, list of tuples, bytes, or file-like objecast.
        If you want to pass a json body pass a dictionary as ``json`` parameter.
        By default this keyword fails if a status code with error values is returned in the response,
        this behavior can be modified using the ``expected_status`` and ``msg`` parameters,
        read more about it in `Status Should Be` keyword documentation.
        In order to disable this implicit assert mechanism you can pass as ``expected_status`` the values ``any`` or
        ``anything``.
        Other optional requests arguments can be passed using ``**kwargs``
        see the `GET` keyword for the complete list.
        """
        response = self._common_request('post', url,
                                        data=data, json=json, **kwargs)
        return response

    @keyword('PUT')
    def session_less_put(self, url, data=None, json=None, **kwargs):
        """
        Sends a PUT request.
        The endpoint used to send the request is the ``url`` parameter, while its body
        can be passed using ``data`` or ``json`` parameters.
        ``data`` can be a dictionary, list of tuples, bytes, or file-like object.
        If you want to pass a json body pass a dictionary as ``json`` parameter.
        By default this keyword fails if a status code with error values is returned in the response,
        this behavior can be modified using the ``expected_status`` and ``msg`` parameters,
        read more about it in `Status Should Be` keyword documentation.
        In order to disable this implicit assert mechanism you can pass as ``expected_status`` the values ``any`` or
        ``anything``.
        Other optional requests arguments can be passed using ``**kwargs``
        see the `GET` keyword for the complete list.
        """

        response = self._common_request("put", url,
                                        data=data, json=json, **kwargs)
        return response

    @keyword('HEAD')
    def session_less_head(self, url, **kwargs):
        """
        Sends a HEAD request.
        The endpoint used to retrieve the HTTP headers is the ``url``.
        ``allow_redirects`` parameter is not provided, it will be set to `False` (as
        opposed to the default behavior).
        By default this keyword fails if a status code with error values is returned in the response,
        this behavior can be modified using the ``expected_status`` and ``msg`` parameters,
        read more about it in `Status Should Be` keyword documentation.
        In order to disable this implicit assert mechanism you can pass as ``expected_status`` the values ``any`` or
        ``anything``.
        Other optional requests arguments can be passed using ``**kwargs``
        see the `GET` keyword for the complete list.
        """
        response = self._common_request('head', url, **kwargs)
        return response

    @keyword('PATCH')
    def session_less_patch(self, url, data=None, json=None, **kwargs):
        """
        Sends a PUT request.
        The endpoint used to send the request is the ``url`` parameter, while its body
        can be passed using ``data`` or ``json`` parameters.
        ``data`` can be a dictionary, list of tuples, bytes, or file-like object.
        If you want to pass a json body pass a dictionary as ``json`` parameter.
        By default this keyword fails if a status code with error values is returned in the response,
        this behavior can be modified using the ``expected_status`` and ``msg`` parameters,
        read more about it in `Status Should Be` keyword documentation.
        In order to disable this implicit assert mechanism you can pass as ``expected_status`` the values ``any`` or
        ``anything``.
        Other optional requests arguments can be passed using ``**kwargs``
        see the `GET` keyword for the complete list.
        """
        response = self._common_request('patch', url,
                                        data=data, json=json, **kwargs)
        return response

    @keyword('DELETE')
    def session_less_delete(self, url, **kwargs):
        """
        Sends a DELETE request.
        The endpoint used to send the request is the ``url`` parameter.
        By default this keyword fails if a status code with error values is returned in the response,
        this behavior can be modified using the ``expected_status`` and ``msg`` parameters,
        read more about it in `Status Should Be` keyword documentation.
        In order to disable this implicit assert mechanism you can pass as ``expected_status`` the values ``any`` or
        ``anything``.
        Other optional requests arguments can be passed using ``**kwargs``
        see the `GET` keyword for the complete list.
        """
        response = self._common_request("delete", url, **kwargs)
        return response

    @keyword('OPTIONS')
    def session_less_options(self, url, **kwargs):
        """
        Sends a OPTIONS request.
        The endpoint used to retrieve the resource is the ``url``.
        By default this keyword fails if a status code with error values is returned in the response,
        this behavior can be modified using the ``expected_status`` and ``msg`` parameters,
        read more about it in `Status Should Be` keyword documentation.
        In order to disable this implicit assert mechanism you can pass as ``expected_status`` the values ``any`` or
        ``anything``.
        Other optional requests arguments can be passed using ``**kwargs``
        see the `GET` keyword for the complete list.
        """
        response = self._common_request("options", url, **kwargs)
        return response

# if __name__ == '__main__':
#     req = requestsKeywords()
#     req.session_less_get('https://api.openweathermap.org/data/2.5/weather?q=Ha&appid=a93c78f714beb362b0438357ad6fe022')
#     req.status_should_be('700')