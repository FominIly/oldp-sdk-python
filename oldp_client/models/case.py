# coding: utf-8

"""
    Open Legal Data API

    With the Open Legal Data API you can access various data from the legal domain, e.g. law text or case files. The data may be used for semantic analysis or to create statistics. For more information visit our website.  # noqa: E501

    OpenAPI spec version: v1
    Contact: api@openlegaldata.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Case(object):
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
        'id': 'int',
        'court_id': 'str',
        'file_number': 'str',
        '_date': 'date',
        'type': 'str',
        'ecli': 'str',
        'content': 'str'
    }

    attribute_map = {
        'id': 'id',
        'court_id': 'court_id',
        'file_number': 'file_number',
        '_date': 'date',
        'type': 'type',
        'ecli': 'ecli',
        'content': 'content'
    }

    def __init__(self, id=None, court_id=None, file_number=None, _date=None, type=None, ecli=None, content=None):  # noqa: E501
        """Case - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._court_id = None
        self._file_number = None
        self.__date = None
        self._type = None
        self._ecli = None
        self._content = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if court_id is not None:
            self.court_id = court_id
        if file_number is not None:
            self.file_number = file_number
        if _date is not None:
            self._date = _date
        if type is not None:
            self.type = type
        if ecli is not None:
            self.ecli = ecli
        self.content = content

    @property
    def id(self):
        """Gets the id of this Case.  # noqa: E501


        :return: The id of this Case.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Case.


        :param id: The id of this Case.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def court_id(self):
        """Gets the court_id of this Case.  # noqa: E501


        :return: The court_id of this Case.  # noqa: E501
        :rtype: str
        """
        return self._court_id

    @court_id.setter
    def court_id(self, court_id):
        """Sets the court_id of this Case.


        :param court_id: The court_id of this Case.  # noqa: E501
        :type: str
        """

        self._court_id = court_id

    @property
    def file_number(self):
        """Gets the file_number of this Case.  # noqa: E501

        File number as defined by court  # noqa: E501

        :return: The file_number of this Case.  # noqa: E501
        :rtype: str
        """
        return self._file_number

    @file_number.setter
    def file_number(self, file_number):
        """Sets the file_number of this Case.

        File number as defined by court  # noqa: E501

        :param file_number: The file_number of this Case.  # noqa: E501
        :type: str
        """
        if file_number is not None and len(file_number) > 100:
            raise ValueError("Invalid value for `file_number`, length must be less than or equal to `100`")  # noqa: E501

        self._file_number = file_number

    @property
    def _date(self):
        """Gets the _date of this Case.  # noqa: E501

        Publication date as in source  # noqa: E501

        :return: The _date of this Case.  # noqa: E501
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this Case.

        Publication date as in source  # noqa: E501

        :param _date: The _date of this Case.  # noqa: E501
        :type: date
        """

        self.__date = _date

    @property
    def type(self):
        """Gets the type of this Case.  # noqa: E501

        Type of decision (Urteil, Beschluss, ...)  # noqa: E501

        :return: The type of this Case.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Case.

        Type of decision (Urteil, Beschluss, ...)  # noqa: E501

        :param type: The type of this Case.  # noqa: E501
        :type: str
        """
        if type is not None and len(type) > 100:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `100`")  # noqa: E501

        self._type = type

    @property
    def ecli(self):
        """Gets the ecli of this Case.  # noqa: E501

        European Case Law Identifier  # noqa: E501

        :return: The ecli of this Case.  # noqa: E501
        :rtype: str
        """
        return self._ecli

    @ecli.setter
    def ecli(self, ecli):
        """Sets the ecli of this Case.

        European Case Law Identifier  # noqa: E501

        :param ecli: The ecli of this Case.  # noqa: E501
        :type: str
        """
        if ecli is not None and len(ecli) > 255:
            raise ValueError("Invalid value for `ecli`, length must be less than or equal to `255`")  # noqa: E501

        self._ecli = ecli

    @property
    def content(self):
        """Gets the content of this Case.  # noqa: E501

        Case full-text formatted in Legal HTML  # noqa: E501

        :return: The content of this Case.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Case.

        Case full-text formatted in Legal HTML  # noqa: E501

        :param content: The content of this Case.  # noqa: E501
        :type: str
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Case, dict):
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
        if not isinstance(other, Case):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
