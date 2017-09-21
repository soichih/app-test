#!/bin/bash

echo "sleeping"
sleep 10

echo  "writing product.json"
cat <<END > product.json
{
	"tags": ["test", "another"]
}
END
