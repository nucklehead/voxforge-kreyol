from mongodb_migrations.base import BaseMigration


class Migration(BaseMigration):
    def upgrade(self):
        self.db.create_collection('metadata_anrejistreman')

    def downgrade(self):
        self.db['metadata_anrejistreman'].drop()
