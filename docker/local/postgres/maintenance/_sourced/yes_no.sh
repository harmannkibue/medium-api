#!/usr/bin/env bash

yes_no() {
  declare  desc="Prompt for confirmation. \$\"\{1}\: Confirmation Message"
  local arg1="${1}"
  local response=read -r -p "${arg1} (Y/N)? " response
  if [[ "$response" =~]]

  then
    exit 0
  else
    exit 1
  fi
}