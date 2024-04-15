# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "compute-diagnostic spot-placement-recommender generate",
)
class Generate(AAZCommand):
    """Generates placement scores for Spot VM skus.

    :example: generate spot vm placement score example
        az compute diagnostic spot-placement-recommender generate -l eastus --subscription ffffffff-ffff-ffff-ffff-ffffffffffff --availability-zones true --desired-locations '["eastus", "eastus2"]' --desired-count 1 --desired-sizes '[{"sku": "Standard_D2_v2"}]'
    """

    _aaz_info = {
        "version": "2024-03-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.compute/locations/{}/diagnostics/spotplacementrecommender/generate", "2024-03-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            required=True,
            id_part="name",
        )

        # define Arg Group "SpotPlacementRecommenderInput"

        _args_schema = cls._args_schema
        _args_schema.availability_zones = AAZBoolArg(
            options=["--availability-zones"],
            arg_group="SpotPlacementRecommenderInput",
            help="Defines if the scope is zonal or regional.",
        )
        _args_schema.desired_count = AAZIntArg(
            options=["--desired-count"],
            arg_group="SpotPlacementRecommenderInput",
            help="Desired instance count per region/zone based on the scope.",
        )
        _args_schema.desired_locations = AAZListArg(
            options=["--desired-locations"],
            arg_group="SpotPlacementRecommenderInput",
            help="The desired regions",
        )
        _args_schema.desired_sizes = AAZListArg(
            options=["--desired-sizes"],
            arg_group="SpotPlacementRecommenderInput",
            help="The desired resource SKUs.",
        )

        desired_locations = cls._args_schema.desired_locations
        desired_locations.Element = AAZStrArg()

        desired_sizes = cls._args_schema.desired_sizes
        desired_sizes.Element = AAZObjectArg()

        _element = cls._args_schema.desired_sizes.Element
        _element.sku = AAZStrArg(
            options=["sku"],
            help="The resource's CRP virtual machine SKU size.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.SpotPlacementRecommenderPost(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class SpotPlacementRecommenderPost(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/diagnostics/spotPlacementRecommender/generate",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "location", self.ctx.args.location,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-03-01-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("availabilityZones", AAZBoolType, ".availability_zones")
            _builder.set_prop("desiredCount", AAZIntType, ".desired_count")
            _builder.set_prop("desiredLocations", AAZListType, ".desired_locations")
            _builder.set_prop("desiredSizes", AAZListType, ".desired_sizes")

            desired_locations = _builder.get(".desiredLocations")
            if desired_locations is not None:
                desired_locations.set_elements(AAZStrType, ".")

            desired_sizes = _builder.get(".desiredSizes")
            if desired_sizes is not None:
                desired_sizes.set_elements(AAZObjectType, ".")

            _elements = _builder.get(".desiredSizes[]")
            if _elements is not None:
                _elements.set_prop("sku", AAZStrType, ".sku")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.availability_zones = AAZBoolType(
                serialized_name="availabilityZones",
            )
            _schema_on_200.desired_count = AAZIntType(
                serialized_name="desiredCount",
            )
            _schema_on_200.desired_locations = AAZListType(
                serialized_name="desiredLocations",
            )
            _schema_on_200.desired_sizes = AAZListType(
                serialized_name="desiredSizes",
            )
            _schema_on_200.placement_scores = AAZListType(
                serialized_name="placementScores",
            )

            desired_locations = cls._schema_on_200.desired_locations
            desired_locations.Element = AAZStrType()

            desired_sizes = cls._schema_on_200.desired_sizes
            desired_sizes.Element = AAZObjectType()

            _element = cls._schema_on_200.desired_sizes.Element
            _element.sku = AAZStrType()

            placement_scores = cls._schema_on_200.placement_scores
            placement_scores.Element = AAZObjectType()

            _element = cls._schema_on_200.placement_scores.Element
            _element.availability_zone = AAZStrType(
                serialized_name="availabilityZone",
            )
            _element.is_quota_available = AAZBoolType(
                serialized_name="isQuotaAvailable",
            )
            _element.region = AAZStrType()
            _element.score = AAZStrType()
            _element.sku = AAZStrType()

            return cls._schema_on_200


class _GenerateHelper:
    """Helper class for Generate"""


__all__ = ["Generate"]
