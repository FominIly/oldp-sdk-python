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


class Court(object):
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
        'name': 'str',
        'court_type': 'str',
        'city': 'int',
        'state': 'int',
        'code': 'str',
        'slug': 'str',
        'description': 'str',
        'image': 'str',
        'homepage': 'str',
        'street_address': 'str',
        'postal_code': 'str',
        'address_locality': 'str',
        'telephone': 'str',
        'fax_number': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'court_type': 'court_type',
        'city': 'city',
        'state': 'state',
        'code': 'code',
        'slug': 'slug',
        'description': 'description',
        'image': 'image',
        'homepage': 'homepage',
        'street_address': 'street_address',
        'postal_code': 'postal_code',
        'address_locality': 'address_locality',
        'telephone': 'telephone',
        'fax_number': 'fax_number'
    }

    def __init__(self, id=None, name=None, court_type=None, city=None, state=None, code=None, slug=None, description=None, image=None, homepage=None, street_address=None, postal_code=None, address_locality=None, telephone=None, fax_number=None):  # noqa: E501
        """Court - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._court_type = None
        self._city = None
        self._state = None
        self._code = None
        self._slug = None
        self._description = None
        self._image = None
        self._homepage = None
        self._street_address = None
        self._postal_code = None
        self._address_locality = None
        self._telephone = None
        self._fax_number = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if court_type is not None:
            self.court_type = court_type
        if city is not None:
            self.city = city
        self.state = state
        self.code = code
        self.slug = slug
        if description is not None:
            self.description = description
        if image is not None:
            self.image = image
        if homepage is not None:
            self.homepage = homepage
        if street_address is not None:
            self.street_address = street_address
        if postal_code is not None:
            self.postal_code = postal_code
        if address_locality is not None:
            self.address_locality = address_locality
        if telephone is not None:
            self.telephone = telephone
        if fax_number is not None:
            self.fax_number = fax_number

    @property
    def id(self):
        """Gets the id of this Court.  # noqa: E501


        :return: The id of this Court.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Court.


        :param id: The id of this Court.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Court.  # noqa: E501

        Full name of the court with location  # noqa: E501

        :return: The name of this Court.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Court.

        Full name of the court with location  # noqa: E501

        :param name: The name of this Court.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501

        self._name = name

    @property
    def court_type(self):
        """Gets the court_type of this Court.  # noqa: E501

        Court type AG,VG,...  # noqa: E501

        :return: The court_type of this Court.  # noqa: E501
        :rtype: str
        """
        return self._court_type

    @court_type.setter
    def court_type(self, court_type):
        """Sets the court_type of this Court.

        Court type AG,VG,...  # noqa: E501

        :param court_type: The court_type of this Court.  # noqa: E501
        :type: str
        """
        if court_type is not None and len(court_type) > 10:
            raise ValueError("Invalid value for `court_type`, length must be less than or equal to `10`")  # noqa: E501

        self._court_type = court_type

    @property
    def city(self):
        """Gets the city of this Court.  # noqa: E501

        Court belongs to this city, if null court is state-level  # noqa: E501

        :return: The city of this Court.  # noqa: E501
        :rtype: int
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Court.

        Court belongs to this city, if null court is state-level  # noqa: E501

        :param city: The city of this Court.  # noqa: E501
        :type: int
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Court.  # noqa: E501

        Court belongs to this state (derive country of this field)  # noqa: E501

        :return: The state of this Court.  # noqa: E501
        :rtype: int
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Court.

        Court belongs to this state (derive country of this field)  # noqa: E501

        :param state: The state of this Court.  # noqa: E501
        :type: int
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501

        self._state = state

    @property
    def code(self):
        """Gets the code of this Court.  # noqa: E501

        Unique court identifier based on ECLI (e.g. BVerfG)  # noqa: E501

        :return: The code of this Court.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Court.

        Unique court identifier based on ECLI (e.g. BVerfG)  # noqa: E501

        :param code: The code of this Court.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if code is not None and len(code) > 20:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `20`")  # noqa: E501

        self._code = code

    @property
    def slug(self):
        """Gets the slug of this Court.  # noqa: E501

        Type & city name as lowercase  # noqa: E501

        :return: The slug of this Court.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Court.

        Type & city name as lowercase  # noqa: E501

        :param slug: The slug of this Court.  # noqa: E501
        :type: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501
        if slug is not None and len(slug) > 60:
            raise ValueError("Invalid value for `slug`, length must be less than or equal to `60`")  # noqa: E501
        if slug is not None and not re.search(r'^[-a-zA-Z0-9_]+$', slug):  # noqa: E501
            raise ValueError(r"Invalid value for `slug`, must be a follow pattern or equal to `/^[-a-zA-Z0-9_]+$/`")  # noqa: E501

        self._slug = slug

    @property
    def description(self):
        """Gets the description of this Court.  # noqa: E501


        :return: The description of this Court.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Court.


        :param description: The description of this Court.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def image(self):
        """Gets the image of this Court.  # noqa: E501


        :return: The image of this Court.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Court.


        :param image: The image of this Court.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def homepage(self):
        """Gets the homepage of this Court.  # noqa: E501

        Official court homepage  # noqa: E501

        :return: The homepage of this Court.  # noqa: E501
        :rtype: str
        """
        return self._homepage

    @homepage.setter
    def homepage(self, homepage):
        """Sets the homepage of this Court.

        Official court homepage  # noqa: E501

        :param homepage: The homepage of this Court.  # noqa: E501
        :type: str
        """
        if homepage is not None and len(homepage) > 200:
            raise ValueError("Invalid value for `homepage`, length must be less than or equal to `200`")  # noqa: E501

        self._homepage = homepage

    @property
    def street_address(self):
        """Gets the street_address of this Court.  # noqa: E501

        Street address with house number  # noqa: E501

        :return: The street_address of this Court.  # noqa: E501
        :rtype: str
        """
        return self._street_address

    @street_address.setter
    def street_address(self, street_address):
        """Sets the street_address of this Court.

        Street address with house number  # noqa: E501

        :param street_address: The street_address of this Court.  # noqa: E501
        :type: str
        """
        if street_address is not None and len(street_address) > 200:
            raise ValueError("Invalid value for `street_address`, length must be less than or equal to `200`")  # noqa: E501

        self._street_address = street_address

    @property
    def postal_code(self):
        """Gets the postal_code of this Court.  # noqa: E501

        Postal code (ZIP code)  # noqa: E501

        :return: The postal_code of this Court.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Court.

        Postal code (ZIP code)  # noqa: E501

        :param postal_code: The postal_code of this Court.  # noqa: E501
        :type: str
        """
        if postal_code is not None and len(postal_code) > 200:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `200`")  # noqa: E501

        self._postal_code = postal_code

    @property
    def address_locality(self):
        """Gets the address_locality of this Court.  # noqa: E501

        Locality (city name)  # noqa: E501

        :return: The address_locality of this Court.  # noqa: E501
        :rtype: str
        """
        return self._address_locality

    @address_locality.setter
    def address_locality(self, address_locality):
        """Sets the address_locality of this Court.

        Locality (city name)  # noqa: E501

        :param address_locality: The address_locality of this Court.  # noqa: E501
        :type: str
        """
        if address_locality is not None and len(address_locality) > 200:
            raise ValueError("Invalid value for `address_locality`, length must be less than or equal to `200`")  # noqa: E501

        self._address_locality = address_locality

    @property
    def telephone(self):
        """Gets the telephone of this Court.  # noqa: E501

        Telephone number  # noqa: E501

        :return: The telephone of this Court.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this Court.

        Telephone number  # noqa: E501

        :param telephone: The telephone of this Court.  # noqa: E501
        :type: str
        """
        if telephone is not None and len(telephone) > 200:
            raise ValueError("Invalid value for `telephone`, length must be less than or equal to `200`")  # noqa: E501

        self._telephone = telephone

    @property
    def fax_number(self):
        """Gets the fax_number of this Court.  # noqa: E501

        Fax number  # noqa: E501

        :return: The fax_number of this Court.  # noqa: E501
        :rtype: str
        """
        return self._fax_number

    @fax_number.setter
    def fax_number(self, fax_number):
        """Sets the fax_number of this Court.

        Fax number  # noqa: E501

        :param fax_number: The fax_number of this Court.  # noqa: E501
        :type: str
        """
        if fax_number is not None and len(fax_number) > 200:
            raise ValueError("Invalid value for `fax_number`, length must be less than or equal to `200`")  # noqa: E501

        self._fax_number = fax_number

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
        if issubclass(Court, dict):
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
        if not isinstance(other, Court):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
