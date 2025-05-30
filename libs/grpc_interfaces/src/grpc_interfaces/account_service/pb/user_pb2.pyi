"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright (C) 2022-2025 Intel Corporation
LIMITED EDGE SOFTWARE DISTRIBUTION LICENSE
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import user_common_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class UserIdRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    user_id: builtins.str
    organization_id: builtins.str
    def __init__(
        self,
        *,
        user_id: builtins.str = ...,
        organization_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id", "user_id", b"user_id"]) -> None: ...

global___UserIdRequest = UserIdRequest

@typing.final
class UserExtIdRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    id: builtins.str
    def __init__(
        self,
        *,
        id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["id", b"id"]) -> None: ...

global___UserExtIdRequest = UserExtIdRequest

@typing.final
class FindUserRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIRST_NAME_FIELD_NUMBER: builtins.int
    SECOND_NAME_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    EXTERNAL_ID_FIELD_NUMBER: builtins.int
    COUNTRY_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    LAST_SUCCESSFUL_LOGIN_FROM_FIELD_NUMBER: builtins.int
    LAST_SUCCESSFUL_LOGIN_TO_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    WORKSPACE_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    CREATED_AT_FROM_FIELD_NUMBER: builtins.int
    CREATED_AT_TO_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FROM_FIELD_NUMBER: builtins.int
    MODIFIED_AT_TO_FIELD_NUMBER: builtins.int
    MODIFIED_BY_FIELD_NUMBER: builtins.int
    SKIP_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    SORT_BY_FIELD_NUMBER: builtins.int
    SORT_DIRECTION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    first_name: builtins.str
    second_name: builtins.str
    email: builtins.str
    external_id: builtins.str
    country: builtins.str
    status: builtins.str
    role: builtins.str
    resource_id: builtins.str
    workspace_id: builtins.str
    organization_id: builtins.str
    created_by: builtins.str
    modified_by: builtins.str
    skip: builtins.int
    limit: builtins.int
    sort_by: builtins.str
    """attribute name"""
    sort_direction: builtins.str
    """asc/desc"""
    name: builtins.str
    """user to search for first name OR second name OR email"""
    @property
    def last_successful_login_from(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def last_successful_login_to(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def resource_type(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def created_at_from(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def created_at_to(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def modified_at_from(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def modified_at_to(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        first_name: builtins.str = ...,
        second_name: builtins.str = ...,
        email: builtins.str = ...,
        external_id: builtins.str = ...,
        country: builtins.str = ...,
        status: builtins.str = ...,
        last_successful_login_from: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        last_successful_login_to: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        role: builtins.str = ...,
        resource_type: collections.abc.Iterable[builtins.str] | None = ...,
        resource_id: builtins.str = ...,
        workspace_id: builtins.str = ...,
        organization_id: builtins.str = ...,
        created_at_from: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_at_to: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_by: builtins.str = ...,
        modified_at_from: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_at_to: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_by: builtins.str = ...,
        skip: builtins.int = ...,
        limit: builtins.int = ...,
        sort_by: builtins.str = ...,
        sort_direction: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at_from", b"created_at_from", "created_at_to", b"created_at_to", "last_successful_login_from", b"last_successful_login_from", "last_successful_login_to", b"last_successful_login_to", "modified_at_from", b"modified_at_from", "modified_at_to", b"modified_at_to"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["country", b"country", "created_at_from", b"created_at_from", "created_at_to", b"created_at_to", "created_by", b"created_by", "email", b"email", "external_id", b"external_id", "first_name", b"first_name", "last_successful_login_from", b"last_successful_login_from", "last_successful_login_to", b"last_successful_login_to", "limit", b"limit", "modified_at_from", b"modified_at_from", "modified_at_to", b"modified_at_to", "modified_by", b"modified_by", "name", b"name", "organization_id", b"organization_id", "resource_id", b"resource_id", "resource_type", b"resource_type", "role", b"role", "second_name", b"second_name", "skip", b"skip", "sort_by", b"sort_by", "sort_direction", b"sort_direction", "status", b"status", "workspace_id", b"workspace_id"]) -> None: ...

global___FindUserRequest = FindUserRequest

@typing.final
class ListUsersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class NextPage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SKIP_FIELD_NUMBER: builtins.int
        LIMIT_FIELD_NUMBER: builtins.int
        skip: builtins.int
        limit: builtins.int
        def __init__(
            self,
            *,
            skip: builtins.int = ...,
            limit: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["limit", b"limit", "skip", b"skip"]) -> None: ...

    USERS_FIELD_NUMBER: builtins.int
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    TOTAL_MATCHED_COUNT_FIELD_NUMBER: builtins.int
    NEXT_PAGE_FIELD_NUMBER: builtins.int
    total_count: builtins.int
    total_matched_count: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[user_common_pb2.UserData]: ...
    @property
    def next_page(self) -> global___ListUsersResponse.NextPage: ...
    def __init__(
        self,
        *,
        users: collections.abc.Iterable[user_common_pb2.UserData] | None = ...,
        total_count: builtins.int = ...,
        total_matched_count: builtins.int = ...,
        next_page: global___ListUsersResponse.NextPage | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_next_page", b"_next_page", "next_page", b"next_page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_next_page", b"_next_page", "next_page", b"next_page", "total_count", b"total_count", "total_matched_count", b"total_matched_count", "users", b"users"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_next_page", b"_next_page"]) -> typing.Literal["next_page"] | None: ...

global___ListUsersResponse = ListUsersResponse

@typing.final
class UserPhotoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_DATA_FIELD_NUMBER: builtins.int
    PHOTO_FIELD_NUMBER: builtins.int
    photo: builtins.bytes
    @property
    def user_data(self) -> global___UserIdRequest: ...
    def __init__(
        self,
        *,
        user_data: global___UserIdRequest | None = ...,
        photo: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["photo", b"photo", "request", b"request", "user_data", b"user_data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["photo", b"photo", "request", b"request", "user_data", b"user_data"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["request", b"request"]) -> typing.Literal["user_data", "photo"] | None: ...

global___UserPhotoRequest = UserPhotoRequest

@typing.final
class UserRolesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLES_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    user_id: builtins.str
    organization_id: builtins.str
    @property
    def roles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[user_common_pb2.UserRoleOperation]: ...
    def __init__(
        self,
        *,
        roles: collections.abc.Iterable[user_common_pb2.UserRoleOperation] | None = ...,
        user_id: builtins.str = ...,
        organization_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id", "roles", b"roles", "user_id", b"user_id"]) -> None: ...

global___UserRolesRequest = UserRolesRequest

@typing.final
class UserGetRolesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    user_id: builtins.str
    organization_id: builtins.str
    resource_type: builtins.str
    def __init__(
        self,
        *,
        user_id: builtins.str = ...,
        organization_id: builtins.str = ...,
        resource_type: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id", "resource_type", b"resource_type", "user_id", b"user_id"]) -> None: ...

global___UserGetRolesRequest = UserGetRolesRequest

@typing.final
class UserRolesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLES_FIELD_NUMBER: builtins.int
    @property
    def roles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[user_common_pb2.UserRole]: ...
    def __init__(
        self,
        *,
        roles: collections.abc.Iterable[user_common_pb2.UserRole] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["roles", b"roles"]) -> None: ...

global___UserRolesResponse = UserRolesResponse

@typing.final
class OrganizationExtended(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_NAME_FIELD_NUMBER: builtins.int
    USER_STATUS_FIELD_NUMBER: builtins.int
    ORGANIZATION_STATUS_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_CREATED_AT_FIELD_NUMBER: builtins.int
    organization_name: builtins.str
    user_status: builtins.str
    organization_status: builtins.str
    organization_id: builtins.str
    @property
    def organization_created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        organization_name: builtins.str = ...,
        user_status: builtins.str = ...,
        organization_status: builtins.str = ...,
        organization_id: builtins.str = ...,
        organization_created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["organization_created_at", b"organization_created_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["organization_created_at", b"organization_created_at", "organization_id", b"organization_id", "organization_name", b"organization_name", "organization_status", b"organization_status", "user_status", b"user_status"]) -> None: ...

global___OrganizationExtended = OrganizationExtended

@typing.final
class UserProfileData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_STATUS_FIELD_NUMBER: builtins.int
    ORGANIZATIONS_FIELD_NUMBER: builtins.int
    TELEMETRY_CONSENT_FIELD_NUMBER: builtins.int
    TELEMETRY_CONSENT_AT_FIELD_NUMBER: builtins.int
    USER_CONSENT_FIELD_NUMBER: builtins.int
    USER_CONSENT_AT_FIELD_NUMBER: builtins.int
    status: builtins.str
    organization_id: builtins.str
    organization_status: builtins.str
    telemetry_consent: builtins.str
    user_consent: builtins.str
    @property
    def organizations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___OrganizationExtended]: ...
    @property
    def telemetry_consent_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def user_consent_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        status: builtins.str | None = ...,
        organization_id: builtins.str | None = ...,
        organization_status: builtins.str | None = ...,
        organizations: collections.abc.Iterable[global___OrganizationExtended] | None = ...,
        telemetry_consent: builtins.str | None = ...,
        telemetry_consent_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        user_consent: builtins.str | None = ...,
        user_consent_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_organization_id", b"_organization_id", "_organization_status", b"_organization_status", "_status", b"_status", "_telemetry_consent", b"_telemetry_consent", "_user_consent", b"_user_consent", "organization_id", b"organization_id", "organization_status", b"organization_status", "status", b"status", "telemetry_consent", b"telemetry_consent", "telemetry_consent_at", b"telemetry_consent_at", "user_consent", b"user_consent", "user_consent_at", b"user_consent_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_organization_id", b"_organization_id", "_organization_status", b"_organization_status", "_status", b"_status", "_telemetry_consent", b"_telemetry_consent", "_user_consent", b"_user_consent", "organization_id", b"organization_id", "organization_status", b"organization_status", "organizations", b"organizations", "status", b"status", "telemetry_consent", b"telemetry_consent", "telemetry_consent_at", b"telemetry_consent_at", "user_consent", b"user_consent", "user_consent_at", b"user_consent_at"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_organization_id", b"_organization_id"]) -> typing.Literal["organization_id"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_organization_status", b"_organization_status"]) -> typing.Literal["organization_status"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_status", b"_status"]) -> typing.Literal["status"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_telemetry_consent", b"_telemetry_consent"]) -> typing.Literal["telemetry_consent"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_user_consent", b"_user_consent"]) -> typing.Literal["user_consent"] | None: ...

global___UserProfileData = UserProfileData

@typing.final
class ActiveUserData(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    FIRST_NAME_FIELD_NUMBER: builtins.int
    SECOND_NAME_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_STATUS_FIELD_NUMBER: builtins.int
    ROLES_FIELD_NUMBER: builtins.int
    LAST_SUCCESSFUL_LOGIN_FIELD_NUMBER: builtins.int
    CURRENT_SUCCESSFUL_LOGIN_FIELD_NUMBER: builtins.int
    TELEMETRY_CONSENT_FIELD_NUMBER: builtins.int
    USER_CONSENT_FIELD_NUMBER: builtins.int
    id: builtins.str
    first_name: builtins.str
    second_name: builtins.str
    email: builtins.str
    status: builtins.str
    organization_id: builtins.str
    organization_status: builtins.str
    telemetry_consent: builtins.str
    user_consent: builtins.str
    @property
    def roles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[user_common_pb2.UserRole]: ...
    @property
    def last_successful_login(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def current_successful_login(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        first_name: builtins.str = ...,
        second_name: builtins.str = ...,
        email: builtins.str = ...,
        status: builtins.str = ...,
        organization_id: builtins.str = ...,
        organization_status: builtins.str = ...,
        roles: collections.abc.Iterable[user_common_pb2.UserRole] | None = ...,
        last_successful_login: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        current_successful_login: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        telemetry_consent: builtins.str | None = ...,
        user_consent: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_telemetry_consent", b"_telemetry_consent", "_user_consent", b"_user_consent", "current_successful_login", b"current_successful_login", "last_successful_login", b"last_successful_login", "telemetry_consent", b"telemetry_consent", "user_consent", b"user_consent"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_telemetry_consent", b"_telemetry_consent", "_user_consent", b"_user_consent", "current_successful_login", b"current_successful_login", "email", b"email", "first_name", b"first_name", "id", b"id", "last_successful_login", b"last_successful_login", "organization_id", b"organization_id", "organization_status", b"organization_status", "roles", b"roles", "second_name", b"second_name", "status", b"status", "telemetry_consent", b"telemetry_consent", "user_consent", b"user_consent"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_telemetry_consent", b"_telemetry_consent"]) -> typing.Literal["telemetry_consent"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_user_consent", b"_user_consent"]) -> typing.Literal["user_consent"] | None: ...

global___ActiveUserData = ActiveUserData

@typing.final
class UserInvitationResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_ID_FIELD_NUMBER: builtins.int
    user_id: builtins.str
    def __init__(
        self,
        *,
        user_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["user_id", b"user_id"]) -> None: ...

global___UserInvitationResponse = UserInvitationResponse

@typing.final
class UserPayload(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    USER_ID_FIELD_NUMBER: builtins.int
    organization_id: builtins.str
    user_id: builtins.str
    def __init__(
        self,
        *,
        organization_id: builtins.str = ...,
        user_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["organization_id", b"organization_id", "user_id", b"user_id"]) -> None: ...

global___UserPayload = UserPayload

@typing.final
class RolePayload(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLE_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    role: builtins.str
    resource_id: builtins.str
    def __init__(
        self,
        *,
        role: builtins.str = ...,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id", "role", b"role"]) -> None: ...

global___RolePayload = RolePayload

@typing.final
class RolesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROLES_FIELD_NUMBER: builtins.int
    @property
    def roles(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___RolePayload]: ...
    def __init__(
        self,
        *,
        roles: collections.abc.Iterable[global___RolePayload] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["roles", b"roles"]) -> None: ...

global___RolesResponse = RolesResponse

@typing.final
class UserRolePayload(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    USER_FIELD_NUMBER: builtins.int
    ROLE_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    role: builtins.str
    resource_id: builtins.str
    @property
    def user(self) -> global___UserPayload: ...
    def __init__(
        self,
        *,
        user: global___UserPayload | None = ...,
        role: builtins.str = ...,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["user", b"user"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["resource_id", b"resource_id", "role", b"role", "user", b"user"]) -> None: ...

global___UserRolePayload = UserRolePayload

@typing.final
class GetUsersRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIRST_NAME_FIELD_NUMBER: builtins.int
    SECOND_NAME_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    EXTERNAL_ID_FIELD_NUMBER: builtins.int
    COUNTRY_FIELD_NUMBER: builtins.int
    LAST_SUCCESSFUL_LOGIN_FIELD_NUMBER: builtins.int
    CURRENT_SUCCESSFUL_LOGIN_FIELD_NUMBER: builtins.int
    CREATED_AT_FROM_FIELD_NUMBER: builtins.int
    CREATED_AT_TO_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FROM_FIELD_NUMBER: builtins.int
    MODIFIED_AT_TO_FIELD_NUMBER: builtins.int
    USER_CONSENT_FROM_FIELD_NUMBER: builtins.int
    USER_CONSENT_TO_FIELD_NUMBER: builtins.int
    SKIP_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    SORT_BY_FIELD_NUMBER: builtins.int
    SORT_DIRECTION_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    first_name: builtins.str
    second_name: builtins.str
    email: builtins.str
    external_id: builtins.str
    country: builtins.str
    skip: builtins.int
    limit: builtins.int
    sort_by: builtins.str
    """attribute name"""
    sort_direction: builtins.str
    """asc/desc"""
    name: builtins.str
    """user to search for first name OR second name OR email"""
    @property
    def last_successful_login(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def current_successful_login(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def created_at_from(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def created_at_to(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def modified_at_from(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def modified_at_to(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def user_consent_from(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def user_consent_to(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        first_name: builtins.str = ...,
        second_name: builtins.str = ...,
        email: builtins.str = ...,
        external_id: builtins.str = ...,
        country: builtins.str = ...,
        last_successful_login: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        current_successful_login: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_at_from: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_at_to: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_at_from: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_at_to: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        user_consent_from: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        user_consent_to: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        skip: builtins.int = ...,
        limit: builtins.int = ...,
        sort_by: builtins.str = ...,
        sort_direction: builtins.str = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at_from", b"created_at_from", "created_at_to", b"created_at_to", "current_successful_login", b"current_successful_login", "last_successful_login", b"last_successful_login", "modified_at_from", b"modified_at_from", "modified_at_to", b"modified_at_to", "user_consent_from", b"user_consent_from", "user_consent_to", b"user_consent_to"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["country", b"country", "created_at_from", b"created_at_from", "created_at_to", b"created_at_to", "current_successful_login", b"current_successful_login", "email", b"email", "external_id", b"external_id", "first_name", b"first_name", "last_successful_login", b"last_successful_login", "limit", b"limit", "modified_at_from", b"modified_at_from", "modified_at_to", b"modified_at_to", "name", b"name", "second_name", b"second_name", "skip", b"skip", "sort_by", b"sort_by", "sort_direction", b"sort_direction", "user_consent_from", b"user_consent_from", "user_consent_to", b"user_consent_to"]) -> None: ...

global___GetUsersRequest = GetUsersRequest

@typing.final
class UserResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    FIRST_NAME_FIELD_NUMBER: builtins.int
    SECOND_NAME_FIELD_NUMBER: builtins.int
    EMAIL_FIELD_NUMBER: builtins.int
    EXTERNAL_ID_FIELD_NUMBER: builtins.int
    COUNTRY_FIELD_NUMBER: builtins.int
    PHOTO_LOCATION_FIELD_NUMBER: builtins.int
    REGISTRATION_TOKEN_FIELD_NUMBER: builtins.int
    LAST_SUCCESSFUL_LOGIN_FIELD_NUMBER: builtins.int
    CURRENT_SUCCESSFUL_LOGIN_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    MODIFIED_AT_FIELD_NUMBER: builtins.int
    MODIFIED_BY_FIELD_NUMBER: builtins.int
    TELEMETRY_CONSENT_FIELD_NUMBER: builtins.int
    TELEMETRY_CONSENT_AT_FIELD_NUMBER: builtins.int
    USER_CONSENT_FIELD_NUMBER: builtins.int
    USER_CONSENT_AT_FIELD_NUMBER: builtins.int
    id: builtins.str
    first_name: builtins.str
    second_name: builtins.str
    email: builtins.str
    external_id: builtins.str
    country: builtins.str
    photo_location: builtins.str
    registration_token: builtins.str
    created_by: builtins.str
    modified_by: builtins.str
    telemetry_consent: builtins.str
    user_consent: builtins.str
    @property
    def last_successful_login(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def current_successful_login(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def telemetry_consent_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def user_consent_at(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        first_name: builtins.str = ...,
        second_name: builtins.str = ...,
        email: builtins.str = ...,
        external_id: builtins.str = ...,
        country: builtins.str = ...,
        photo_location: builtins.str = ...,
        registration_token: builtins.str = ...,
        last_successful_login: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        current_successful_login: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        created_by: builtins.str = ...,
        modified_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        modified_by: builtins.str = ...,
        telemetry_consent: builtins.str | None = ...,
        telemetry_consent_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        user_consent: builtins.str | None = ...,
        user_consent_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_telemetry_consent", b"_telemetry_consent", "_user_consent", b"_user_consent", "created_at", b"created_at", "current_successful_login", b"current_successful_login", "last_successful_login", b"last_successful_login", "modified_at", b"modified_at", "telemetry_consent", b"telemetry_consent", "telemetry_consent_at", b"telemetry_consent_at", "user_consent", b"user_consent", "user_consent_at", b"user_consent_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_telemetry_consent", b"_telemetry_consent", "_user_consent", b"_user_consent", "country", b"country", "created_at", b"created_at", "created_by", b"created_by", "current_successful_login", b"current_successful_login", "email", b"email", "external_id", b"external_id", "first_name", b"first_name", "id", b"id", "last_successful_login", b"last_successful_login", "modified_at", b"modified_at", "modified_by", b"modified_by", "photo_location", b"photo_location", "registration_token", b"registration_token", "second_name", b"second_name", "telemetry_consent", b"telemetry_consent", "telemetry_consent_at", b"telemetry_consent_at", "user_consent", b"user_consent", "user_consent_at", b"user_consent_at"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_telemetry_consent", b"_telemetry_consent"]) -> typing.Literal["telemetry_consent"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_user_consent", b"_user_consent"]) -> typing.Literal["user_consent"] | None: ...

global___UserResponse = UserResponse

@typing.final
class ListGetUsersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class NextPage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SKIP_FIELD_NUMBER: builtins.int
        LIMIT_FIELD_NUMBER: builtins.int
        skip: builtins.int
        limit: builtins.int
        def __init__(
            self,
            *,
            skip: builtins.int = ...,
            limit: builtins.int = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["limit", b"limit", "skip", b"skip"]) -> None: ...

    USERS_FIELD_NUMBER: builtins.int
    TOTAL_COUNT_FIELD_NUMBER: builtins.int
    TOTAL_MATCHED_COUNT_FIELD_NUMBER: builtins.int
    NEXT_PAGE_FIELD_NUMBER: builtins.int
    total_count: builtins.int
    total_matched_count: builtins.int
    @property
    def users(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___UserResponse]: ...
    @property
    def next_page(self) -> global___ListGetUsersResponse.NextPage: ...
    def __init__(
        self,
        *,
        users: collections.abc.Iterable[global___UserResponse] | None = ...,
        total_count: builtins.int = ...,
        total_matched_count: builtins.int = ...,
        next_page: global___ListGetUsersResponse.NextPage | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_next_page", b"_next_page", "next_page", b"next_page"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_next_page", b"_next_page", "next_page", b"next_page", "total_count", b"total_count", "total_matched_count", b"total_matched_count", "users", b"users"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_next_page", b"_next_page"]) -> typing.Literal["next_page"] | None: ...

global___ListGetUsersResponse = ListGetUsersResponse
