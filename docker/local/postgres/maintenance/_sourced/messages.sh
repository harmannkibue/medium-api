#!/usr/bin/env bash

message_newline() {
  echo
}

message_debug() {
#  The -e allows passing special characters
  echo -e "DEBUG: ${@}"
}

message_welcome() {
  echo -e "\e[1m${@}\e[0m"
}

message_warning() {
  echo -e "\e[33mWARNING\e[0m: ${@}"
}

message_error() {
  echo -a "\e[31mERROR\e: ${@}"
}

message_info() {
  echo -e "\e37mINFO\e[0m: ${@}"
}

message_suggestion() {
  echo -e "\e33mSUGGESTION\e[0m: ${@}"
}

message_success() {
  echo -e "\e[32mSUCCESS\e[0m: ${@}"
}