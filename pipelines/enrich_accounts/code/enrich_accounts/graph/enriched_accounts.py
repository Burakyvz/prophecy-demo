from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from enrich_accounts.config.ConfigStore import *
from enrich_accounts.functions import *

def enriched_accounts(spark: SparkSession, multi_join: DataFrame):
    multi_join.write\
        .format("delta")\
        .option("overwriteSchema", True)\
        .mode("overwrite")\
        .saveAsTable("`hive_metastore`.`default`.`enriched_accounts_demo2`")
