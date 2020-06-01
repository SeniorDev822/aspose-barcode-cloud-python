# coding: utf-8

"""

    Copyright (c) 2020 Aspose.BarCode for Cloud

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.

"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from aspose_barcode_cloud.api_client import ApiClient


class StorageApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_disc_usage(self, storage_name=None, async_req=False, **kwargs):
        """Get disc usage

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = StorageApi().get_disc_usage(async_req=True)
        >>> result = thread.get()

        :param str storage_name: Storage name # noqa: E501
        :param async_req bool
        :return: DiscUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.get_disc_usage_with_http_info(storage_name=storage_name, **kwargs)
        else:
            (data) = self.get_disc_usage_with_http_info(storage_name=storage_name, **kwargs)
            return data

    def get_disc_usage_with_http_info(self, **kwargs):
        """Get disc usage

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = StorageApi().get_disc_usage_with_http_info(async_req=True)
        >>> result = thread.get()

        :return: DiscUsage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"storage_name"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_disc_usage" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "storage_name" in params:
            query_params.append(("storageName", params["storage_name"]))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        # Authentication setting
        auth_settings = ["JWT"]

        return self.api_client.call_api(
            "/barcode/storage/disc",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="DiscUsage",
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_file_versions(self, path, storage_name=None, async_req=False, **kwargs):
        """Get file versions

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = StorageApi().get_file_versions(path, async_req=True)
        >>> result = thread.get()

        :param str path: File path e.g. '/file.ext' # noqa: E501
        :param str storage_name: Storage name # noqa: E501
        :param async_req bool
        :return: FileVersions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.get_file_versions_with_http_info(path, storage_name=storage_name, **kwargs)
        else:
            (data) = self.get_file_versions_with_http_info(path, storage_name=storage_name, **kwargs)
            return data

    def get_file_versions_with_http_info(self, path, **kwargs):
        """Get file versions

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = StorageApi().get_file_versions_with_http_info(path, async_req=True)
        >>> result = thread.get()

        :param str path: File path e.g. '/file.ext' # noqa: E501
        :return: FileVersions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"path", "storage_name"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method get_file_versions" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'path' is set
        if "path" not in params or params["path"] is None:
            raise ValueError("Missing the required parameter `path` when calling `get_file_versions`")

        collection_formats = {}

        path_params = {}
        if "path" in params:
            path_params["path"] = params["path"]

        query_params = []
        if "storage_name" in params:
            query_params.append(("storageName", params["storage_name"]))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        # Authentication setting
        auth_settings = ["JWT"]

        return self.api_client.call_api(
            "/barcode/storage/version/{path}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="FileVersions",
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def object_exists(self, path, storage_name=None, version_id=None, async_req=False, **kwargs):
        """Check if file or folder exists

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = StorageApi().object_exists(path, async_req=True)
        >>> result = thread.get()

        :param str path: File or folder path e.g. '/file.ext' or '/folder' # noqa: E501
        :param str storage_name: Storage name # noqa: E501
        :param str version_id: File version ID # noqa: E501
        :param async_req bool
        :return: ObjectExist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.object_exists_with_http_info(path, storage_name=storage_name, version_id=version_id, **kwargs)
        else:
            (data) = self.object_exists_with_http_info(path, storage_name=storage_name, version_id=version_id, **kwargs)
            return data

    def object_exists_with_http_info(self, path, **kwargs):
        """Check if file or folder exists

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = StorageApi().object_exists_with_http_info(path, async_req=True)
        >>> result = thread.get()

        :param str path: File or folder path e.g. '/file.ext' or '/folder' # noqa: E501
        :return: ObjectExist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"path", "storage_name", "version_id"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method object_exists" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'path' is set
        if "path" not in params or params["path"] is None:
            raise ValueError("Missing the required parameter `path` when calling `object_exists`")

        collection_formats = {}

        path_params = {}
        if "path" in params:
            path_params["path"] = params["path"]

        query_params = []
        if "storage_name" in params:
            query_params.append(("storageName", params["storage_name"]))
        if "version_id" in params:
            query_params.append(("versionId", params["version_id"]))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        # Authentication setting
        auth_settings = ["JWT"]

        return self.api_client.call_api(
            "/barcode/storage/exist/{path}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ObjectExist",
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def storage_exists(self, storage_name, async_req=False, **kwargs):
        """Check if storage exists

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = StorageApi().storage_exists(storage_name, async_req=True)
        >>> result = thread.get()

        :param str storage_name: Storage name # noqa: E501
        :param async_req bool
        :return: StorageExist
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if async_req:
            return self.storage_exists_with_http_info(storage_name, **kwargs)
        else:
            (data) = self.storage_exists_with_http_info(storage_name, **kwargs)
            return data

    def storage_exists_with_http_info(self, storage_name, **kwargs):
        """Check if storage exists

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = StorageApi().storage_exists_with_http_info(storage_name, async_req=True)
        >>> result = thread.get()

        :param str storage_name: Storage name # noqa: E501
        :return: StorageExist
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = {"storage_name"}
        all_params.add("async_req")
        all_params.add("_return_http_data_only")
        all_params.add("_preload_content")
        all_params.add("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError("Got an unexpected keyword argument '%s'" " to method storage_exists" % key)
            if val is None:
                continue

            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'storage_name' is set
        if "storage_name" not in params or params["storage_name"] is None:
            raise ValueError("Missing the required parameter `storage_name` when calling `storage_exists`")

        collection_formats = {}

        path_params = {}
        if "storage_name" in params:
            path_params["storageName"] = params["storage_name"]

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # HTTP header `Content-Type`
        header_params["Content-Type"] = self.api_client.select_header_content_type(["application/json"])

        # Authentication setting
        auth_settings = ["JWT"]

        return self.api_client.call_api(
            "/barcode/storage/{storageName}/exist",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="StorageExist",
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
