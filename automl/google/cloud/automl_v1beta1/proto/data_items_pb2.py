# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/data_items.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.automl_v1beta1.proto import (
    io_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_io__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/data_items.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1"
    ),
    serialized_pb=_b(
        '\n2google/cloud/automl_v1beta1/proto/data_items.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a*google/cloud/automl_v1beta1/proto/io.proto"\x7f\n\x05Image\x12\x15\n\x0bimage_bytes\x18\x01 \x01(\x0cH\x00\x12@\n\x0cinput_config\x18\x06 \x01(\x0b\x32(.google.cloud.automl.v1beta1.InputConfigH\x00\x12\x15\n\rthumbnail_uri\x18\x04 \x01(\tB\x06\n\x04\x64\x61ta"F\n\x0bTextSnippet\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x11\n\tmime_type\x18\x02 \x01(\t\x12\x13\n\x0b\x63ontent_uri\x18\x04 \x01(\t"\x92\x01\n\x0e\x45xamplePayload\x12\x33\n\x05image\x18\x01 \x01(\x0b\x32".google.cloud.automl.v1beta1.ImageH\x00\x12@\n\x0ctext_snippet\x18\x02 \x01(\x0b\x32(.google.cloud.automl.v1beta1.TextSnippetH\x00\x42\t\n\x07payloadB\x84\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_io__pb2.DESCRIPTOR,
    ],
)


_IMAGE = _descriptor.Descriptor(
    name="Image",
    full_name="google.cloud.automl.v1beta1.Image",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="image_bytes",
            full_name="google.cloud.automl.v1beta1.Image.image_bytes",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="input_config",
            full_name="google.cloud.automl.v1beta1.Image.input_config",
            index=1,
            number=6,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="thumbnail_uri",
            full_name="google.cloud.automl.v1beta1.Image.thumbnail_uri",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="data",
            full_name="google.cloud.automl.v1beta1.Image.data",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=157,
    serialized_end=284,
)


_TEXTSNIPPET = _descriptor.Descriptor(
    name="TextSnippet",
    full_name="google.cloud.automl.v1beta1.TextSnippet",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="content",
            full_name="google.cloud.automl.v1beta1.TextSnippet.content",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="mime_type",
            full_name="google.cloud.automl.v1beta1.TextSnippet.mime_type",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="content_uri",
            full_name="google.cloud.automl.v1beta1.TextSnippet.content_uri",
            index=2,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=286,
    serialized_end=356,
)


_EXAMPLEPAYLOAD = _descriptor.Descriptor(
    name="ExamplePayload",
    full_name="google.cloud.automl.v1beta1.ExamplePayload",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="image",
            full_name="google.cloud.automl.v1beta1.ExamplePayload.image",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="text_snippet",
            full_name="google.cloud.automl.v1beta1.ExamplePayload.text_snippet",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="payload",
            full_name="google.cloud.automl.v1beta1.ExamplePayload.payload",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=359,
    serialized_end=505,
)

_IMAGE.fields_by_name[
    "input_config"
].message_type = google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_io__pb2._INPUTCONFIG
_IMAGE.oneofs_by_name["data"].fields.append(_IMAGE.fields_by_name["image_bytes"])
_IMAGE.fields_by_name["image_bytes"].containing_oneof = _IMAGE.oneofs_by_name["data"]
_IMAGE.oneofs_by_name["data"].fields.append(_IMAGE.fields_by_name["input_config"])
_IMAGE.fields_by_name["input_config"].containing_oneof = _IMAGE.oneofs_by_name["data"]
_EXAMPLEPAYLOAD.fields_by_name["image"].message_type = _IMAGE
_EXAMPLEPAYLOAD.fields_by_name["text_snippet"].message_type = _TEXTSNIPPET
_EXAMPLEPAYLOAD.oneofs_by_name["payload"].fields.append(
    _EXAMPLEPAYLOAD.fields_by_name["image"]
)
_EXAMPLEPAYLOAD.fields_by_name[
    "image"
].containing_oneof = _EXAMPLEPAYLOAD.oneofs_by_name["payload"]
_EXAMPLEPAYLOAD.oneofs_by_name["payload"].fields.append(
    _EXAMPLEPAYLOAD.fields_by_name["text_snippet"]
)
_EXAMPLEPAYLOAD.fields_by_name[
    "text_snippet"
].containing_oneof = _EXAMPLEPAYLOAD.oneofs_by_name["payload"]
DESCRIPTOR.message_types_by_name["Image"] = _IMAGE
DESCRIPTOR.message_types_by_name["TextSnippet"] = _TEXTSNIPPET
DESCRIPTOR.message_types_by_name["ExamplePayload"] = _EXAMPLEPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Image = _reflection.GeneratedProtocolMessageType(
    "Image",
    (_message.Message,),
    dict(
        DESCRIPTOR=_IMAGE,
        __module__="google.cloud.automl_v1beta1.proto.data_items_pb2",
        __doc__="""A representation of an image.
  
  
  Attributes:
      data:
          Input only. The data representing the image. For Predict calls
          [image\_bytes][] must be set, as other options are not
          currently supported by prediction API. You can read the
          contents of an uploaded image by using the [content\_uri][]
          field.
      image_bytes:
          Image content represented as a stream of bytes. Note: As with
          all ``bytes`` fields, protobuffers use a pure binary
          representation, whereas JSON representations use base64.
      input_config:
          An input config specifying the content of the image.
      thumbnail_uri:
          Output only. HTTP URI to the thumbnail image.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.Image)
    ),
)
_sym_db.RegisterMessage(Image)

TextSnippet = _reflection.GeneratedProtocolMessageType(
    "TextSnippet",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TEXTSNIPPET,
        __module__="google.cloud.automl_v1beta1.proto.data_items_pb2",
        __doc__="""A representation of a text snippet.
  
  
  Attributes:
      content:
          Required. The content of the text snippet as a string. Up to
          250000 characters long.
      mime_type:
          The format of the source text. For example, "text/html" or
          "text/plain". If left blank the format is automatically
          determined from the type of the uploaded content. The default
          is "text/html". Up to 25000 characters long.
      content_uri:
          Output only. HTTP URI where you can download the content.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextSnippet)
    ),
)
_sym_db.RegisterMessage(TextSnippet)

ExamplePayload = _reflection.GeneratedProtocolMessageType(
    "ExamplePayload",
    (_message.Message,),
    dict(
        DESCRIPTOR=_EXAMPLEPAYLOAD,
        __module__="google.cloud.automl_v1beta1.proto.data_items_pb2",
        __doc__="""Example data used for training or prediction.
  
  
  Attributes:
      payload:
          Required. Input only. The example data.
      image:
          An example image.
      text_snippet:
          Example text.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.ExamplePayload)
    ),
)
_sym_db.RegisterMessage(ExamplePayload)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
