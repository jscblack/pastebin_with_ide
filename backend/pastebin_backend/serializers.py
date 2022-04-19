from re import M
from rest_framework import serializers
from pastebin_backend.models import *
from jsonschema  import  ValidationError, validate
import time
class CreatePasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paste
        fields = [
            "paste_id",
            "paste_snap",
            # "paste_time",
            # "ip_address",
        ]
    # 校验json格式
    
    def validate_paste_snap(self, value):
        schema  =  {
            "type":"object",
            "properties":{
                "poster" : {
                    "type" :"string",
                },
                "source":{
                    "type" :"string",
                },
                "stdin":{
                    "type" :"string",
                },
                "expect_output":{
                    "type" :"string",
                },
                "stdout":{
                    "type" :"string",
                },
                "stderr":{
                    "type" :"string",
                },
                "compile_output":{
                    "type" :"string",
                },
                "sandbox_message":{
                    "type" :"string",
                },
                "console_output":{
                    "type" :"string",
                },
                "compiler_options":{
                    "type" :"string",
                },
                "command_line":{
                    "type" :"string",
                },
                "language":{
                    "type" :"integer",
                },
                "expire_time":{
                    "type" :"integer",
                },
            },
            "required" : ["poster", "source", "stdin", "expect_output", "stdout", "stderr", "compile_output", "sandbox_message", "console_output", "compiler_options", "command_line", "language", "expire_time"]
        }
        try:
            validate(value, schema)
        except ValidationError as e:
            raise serializers.ValidationError(e.message)
        return value
    # 创建时自动获取ip地址
    def create(self, validated_data):
        validated_data['ip_address'] = self.context['request'].META['REMOTE_ADDR']
        # #解析json
        # paste_snap = validated_data['paste_snap']
        # #获取过期时间
        # expire_time = paste_snap['expire_time']
        print(validated_data['paste_snap'])
        # 自动更新expire_time
        if validated_data['paste_snap']['expire_time']==-1:
            validated_data['expire_time']=2147483647
        else:
            validated_data['expire_time'] = int(time.time()) + int(validated_data['paste_snap']['expire_time'])*3600
        return super().create(validated_data)


class GetPasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paste
        fields = [
            # "paste_id",
            "paste_snap",
            "paste_time",
            "expire_time",
            # "ip_address",
        ]
    