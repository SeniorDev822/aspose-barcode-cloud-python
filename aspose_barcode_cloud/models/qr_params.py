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


import pprint
import re  # noqa: F401

import six


class QrParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "aspect_ratio": "float",
        "text_encoding": "str",
        "encode_type": "QREncodeType",
        "eci_encoding": "ECIEncodings",
        "encode_mode": "QREncodeMode",
        "error_level": "QRErrorLevel",
        "version": "QRVersion",
    }

    attribute_map = {
        "aspect_ratio": "AspectRatio",
        "text_encoding": "TextEncoding",
        "encode_type": "EncodeType",
        "eci_encoding": "ECIEncoding",
        "encode_mode": "EncodeMode",
        "error_level": "ErrorLevel",
        "version": "Version",
    }

    def __init__(
        self,
        aspect_ratio=None,
        text_encoding=None,
        encode_type=None,
        eci_encoding=None,
        encode_mode=None,
        error_level=None,
        version=None,
    ):  # noqa: E501
        """QrParams - a model defined in Swagger"""  # noqa: E501

        self._aspect_ratio = None
        self._text_encoding = None
        self._encode_type = None
        self._eci_encoding = None
        self._encode_mode = None
        self._error_level = None
        self._version = None
        self.discriminator = None

        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if text_encoding is not None:
            self.text_encoding = text_encoding
        if encode_type is not None:
            self.encode_type = encode_type
        if eci_encoding is not None:
            self.eci_encoding = eci_encoding
        if encode_mode is not None:
            self.encode_mode = encode_mode
        if error_level is not None:
            self.error_level = error_level
        if version is not None:
            self.version = version

    @property
    def aspect_ratio(self):
        """Gets the aspect_ratio of this QrParams.  # noqa: E501

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :return: The aspect_ratio of this QrParams.  # noqa: E501
        :rtype: float
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        """Sets the aspect_ratio of this QrParams.

        Height/Width ratio of 2D BarCode module.  # noqa: E501

        :param aspect_ratio: The aspect_ratio of this QrParams.  # noqa: E501
        :type: float
        """

        self._aspect_ratio = aspect_ratio

    @property
    def text_encoding(self):
        """Gets the text_encoding of this QrParams.  # noqa: E501

        Encoding of codetext.  # noqa: E501

        :return: The text_encoding of this QrParams.  # noqa: E501
        :rtype: str
        """
        return self._text_encoding

    @text_encoding.setter
    def text_encoding(self, text_encoding):
        """Sets the text_encoding of this QrParams.

        Encoding of codetext.  # noqa: E501

        :param text_encoding: The text_encoding of this QrParams.  # noqa: E501
        :type: str
        """

        self._text_encoding = text_encoding

    @property
    def encode_type(self):
        """Gets the encode_type of this QrParams.  # noqa: E501

        QR / MicroQR selector mode. Select ForceQR for standard QR symbols, Auto for MicroQR.  # noqa: E501

        :return: The encode_type of this QrParams.  # noqa: E501
        :rtype: QREncodeType
        """
        return self._encode_type

    @encode_type.setter
    def encode_type(self, encode_type):
        """Sets the encode_type of this QrParams.

        QR / MicroQR selector mode. Select ForceQR for standard QR symbols, Auto for MicroQR.  # noqa: E501

        :param encode_type: The encode_type of this QrParams.  # noqa: E501
        :type: QREncodeType
        """

        self._encode_type = encode_type

    @property
    def eci_encoding(self):
        """Gets the eci_encoding of this QrParams.  # noqa: E501

        Extended Channel Interpretation Identifiers. It is used to tell the barcode reader details about the used references for encoding the data in the symbol. Current implementation consists all well known charset encodings.  # noqa: E501

        :return: The eci_encoding of this QrParams.  # noqa: E501
        :rtype: ECIEncodings
        """
        return self._eci_encoding

    @eci_encoding.setter
    def eci_encoding(self, eci_encoding):
        """Sets the eci_encoding of this QrParams.

        Extended Channel Interpretation Identifiers. It is used to tell the barcode reader details about the used references for encoding the data in the symbol. Current implementation consists all well known charset encodings.  # noqa: E501

        :param eci_encoding: The eci_encoding of this QrParams.  # noqa: E501
        :type: ECIEncodings
        """

        self._eci_encoding = eci_encoding

    @property
    def encode_mode(self):
        """Gets the encode_mode of this QrParams.  # noqa: E501

        QR symbology type of BarCode's encoding mode. Default value: QREncodeMode.Auto.  # noqa: E501

        :return: The encode_mode of this QrParams.  # noqa: E501
        :rtype: QREncodeMode
        """
        return self._encode_mode

    @encode_mode.setter
    def encode_mode(self, encode_mode):
        """Sets the encode_mode of this QrParams.

        QR symbology type of BarCode's encoding mode. Default value: QREncodeMode.Auto.  # noqa: E501

        :param encode_mode: The encode_mode of this QrParams.  # noqa: E501
        :type: QREncodeMode
        """

        self._encode_mode = encode_mode

    @property
    def error_level(self):
        """Gets the error_level of this QrParams.  # noqa: E501

        Level of Reed-Solomon error correction for QR barcode. From low to high: LevelL, LevelM, LevelQ, LevelH. see QRErrorLevel.               # noqa: E501

        :return: The error_level of this QrParams.  # noqa: E501
        :rtype: QRErrorLevel
        """
        return self._error_level

    @error_level.setter
    def error_level(self, error_level):
        """Sets the error_level of this QrParams.

        Level of Reed-Solomon error correction for QR barcode. From low to high: LevelL, LevelM, LevelQ, LevelH. see QRErrorLevel.               # noqa: E501

        :param error_level: The error_level of this QrParams.  # noqa: E501
        :type: QRErrorLevel
        """

        self._error_level = error_level

    @property
    def version(self):
        """Gets the version of this QrParams.  # noqa: E501

        Version of QR Code. From Version1 to Version40 for QR code and from M1 to M4 for MicroQr. Default value is QRVersion.Auto.  # noqa: E501

        :return: The version of this QrParams.  # noqa: E501
        :rtype: QRVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this QrParams.

        Version of QR Code. From Version1 to Version40 for QR code and from M1 to M4 for MicroQr. Default value is QRVersion.Auto.  # noqa: E501

        :param version: The version of this QrParams.  # noqa: E501
        :type: QRVersion
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(QrParams, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, QrParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
