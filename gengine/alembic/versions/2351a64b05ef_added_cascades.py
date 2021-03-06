"""Added Cascades

Revision ID: 2351a64b05ef
Revises: 160e3f4be10a
Create Date: 2015-04-01 09:15:47.490122

"""

# revision identifiers, used by Alembic.
revision = '2351a64b05ef'
down_revision = '3fd502c152c9'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    from sqlalchemy.engine.reflection import Inspector 
    insp = Inspector.from_engine(op.get_bind())
    tables = insp.get_table_names() 
    
    for table in tables:
        fks = insp.get_foreign_keys(table) 
        
        
        for fk in fks:
            op.execute("ALTER TABLE "+table+" DROP CONSTRAINT "+fk["name"])
    
    op.create_foreign_key(None, 'achievements', 'achievementcategories', ['achievementcategory_id'], ['id'], ondelete="SET NULL")
    op.create_foreign_key(None, 'achievements_properties', 'translationvariables', ['value_translation_id'], ['id'], ondelete="RESTRICT")
    op.create_foreign_key(None, 'achievements_properties', 'properties', ['property_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'achievements_properties', 'achievements', ['achievement_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'achievements_rewards', 'achievements', ['achievement_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'achievements_rewards', 'translationvariables', ['value_translation_id'], ['id'], ondelete="RESTRICT")
    op.create_foreign_key(None, 'achievements_rewards', 'rewards', ['reward_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'achievements_users', 'users', ['user_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'achievements_users', 'achievements', ['achievement_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'denials', 'achievements', ['from_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'denials', 'achievements', ['to_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'goal_evaluation_cache', 'goals', ['goal_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'goal_evaluation_cache', 'users', ['user_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'goals', 'translationvariables', ['name_translation_id'], ['id'], ondelete="RESTRICT")
    op.create_foreign_key(None, 'goals', 'achievements', ['achievement_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'requirements', 'achievements', ['to_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'requirements', 'achievements', ['from_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'translations', 'languages', ['language_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'translations', 'translationvariables', ['translationvariable_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'users_groups', 'users', ['user_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'users_groups', 'groups', ['group_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'users_users', 'users', ['to_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'users_users', 'users', ['from_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'values', 'users', ['user_id'], ['id'], ondelete="CASCADE")
    op.create_foreign_key(None, 'values', 'variables', ['variable_id'], ['id'], ondelete="CASCADE")
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    
    from sqlalchemy.engine.reflection import Inspector 
    insp = Inspector.from_engine(op.get_bind())
    tables = insp.get_table_names() 
    
    for table in tables:
        fks = insp.get_foreign_keys(table) 
        
        for fk in fks:
            print "ALTER TABLE "+table+" DROP CONSTRAINT "+fk["name"]
            op.execute("ALTER TABLE "+table+" DROP CONSTRAINT "+fk["name"])
    
    op.create_foreign_key(None, 'achievements', 'achievementcategories', ['achievementcategory_id'], ['id'])
    op.create_foreign_key(None, 'achievements_properties', 'translationvariables', ['value_translation_id'], ['id'])
    op.create_foreign_key(None, 'achievements_properties', 'properties', ['property_id'], ['id'])
    op.create_foreign_key(None, 'achievements_properties', 'achievements', ['achievement_id'], ['id'])
    op.create_foreign_key(None, 'achievements_rewards', 'achievements', ['achievement_id'], ['id'])
    op.create_foreign_key(None, 'achievements_rewards', 'translationvariables', ['value_translation_id'], ['id'])
    op.create_foreign_key(None, 'achievements_rewards', 'rewards', ['reward_id'], ['id'])
    op.create_foreign_key(None, 'achievements_users', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'achievements_users', 'achievements', ['achievement_id'], ['id'])
    op.create_foreign_key(None, 'denials', 'achievements', ['from_id'], ['id'])
    op.create_foreign_key(None, 'denials', 'achievements', ['to_id'], ['id'])
    op.create_foreign_key(None, 'goal_evaluation_cache', 'goals', ['goal_id'], ['id'])
    op.create_foreign_key(None, 'goal_evaluation_cache', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'goals', 'translationvariables', ['name_translation_id'], ['id'])
    op.create_foreign_key(None, 'goals', 'achievements', ['achievement_id'], ['id'])
    op.create_foreign_key(None, 'requirements', 'achievements', ['to_id'], ['id'])
    op.create_foreign_key(None, 'requirements', 'achievements', ['from_id'], ['id'])
    op.create_foreign_key(None, 'translations', 'languages', ['language_id'], ['id'])
    op.create_foreign_key(None, 'translations', 'translationvariables', ['translationvariable_id'], ['id'])
    op.create_foreign_key(None, 'users_groups', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'users_groups', 'groups', ['group_id'], ['id'])
    op.create_foreign_key(None, 'users_users', 'users', ['to_id'], ['id'])
    op.create_foreign_key(None, 'users_users', 'users', ['from_id'], ['id'])
    op.create_foreign_key(None, 'values', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'values', 'variables', ['variable_id'], ['id'])
    
    ### end Alembic commands ###
