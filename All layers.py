# Databricks notebook source
df = spark.sql("select * from metadat_all_layer")
print(df.columns)



# COMMAND ----------

df = df.toDF(*[col.strip() for col in df.columns])
display(df)

# COMMAND ----------


rename_columns = {
    "RawTableName": "raw_table_name",
    "RawTableColumn": "raw_column_name",
    "RawTableColDatatype": "raw_datatype",
    "CuratedTableName": "curated_table_name",
    "CuratedTableColumn": "curated_column_name",
    "CuratedTableColumnDatatype": "curated_datatype",
    "PresntationLayTableName": "presentation_table_name",
    "PresentationLayercolumn": "presentation_column_name",
    "PresentationLayerColDataType": "presentation_datatype"
}

for old_col, new_col in rename_columns.items():
    df = df.withColumnRenamed(old_col, new_col)
display(df)

# COMMAND ----------

from collections import defaultdict
tables = defaultdict(set)

rows = df.collect()

for row in rows:
# raw layer
    if row.raw_table_name and row.raw_column_name and row.raw_datatype:
        table = row.raw_table_name.strip()
        tables[table].add((row.raw_column_name.strip(), row.raw_datatype.strip()))

# COMMAND ----------

#cureated layer
if row.curated_table_name and row.curated_column_name and row.curated_datatype:
    table = row.curated_table_name.strip()
    tables[table].add((row.curated_column_name.strip(), row.curated_datatype.strip()))

# COMMAND ----------

if row.presentation_table_name and row.presentation_column_name and row.presentation_datatype:
    table = row.presentation_table_name.strip()
    tables[table].add((row.presentation_column_name.strip(), row.presentation_datatype.strip()))



# COMMAND ----------

for table_name, columns in tables.items():
    spark.sql(f"DROP TABLE IF EXISTS {table_name}")
    col_defs = ",\n  ".join([f"{col} {dtype}" for col, dtype in columns])
    create_sql = f"CREATE TABLE {table_name} (\n  {col_defs}\n)"
    print(f"Running SQL for: {table_name}")
    spark.sql(create_sql)
    
    