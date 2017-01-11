#!/usr/bin/env python

#
# Generated Tue Jan 10 06:06:46 2017 by generateDS.py version 2.22a.
#
# Command line options:
#   ('-f', '')
#   ('-o', 'app/SCHEMA_LAYOUTS/Shipment-7-6.py')
#   ('-s', 'Shipment.py')
#   ('--super', 'Shipments')
#
# Command line arguments:
#   app/SCHEMAS/Shipment-7.6.xsd
#
# Command line:
#   generateDS/generateDS.py -f -o "app/SCHEMA_LAYOUTS/Shipment-7-6.py" -s "Shipment.py" --super="Shipments" app/SCHEMAS/Shipment-7.6.xsd
#
# Current working directory (os.getcwd()):
#   document-scorecard-v2
#

import sys
from lxml import etree as etree_

import Shipments as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'utf-8'

#
# Data representation classes
#


class ShipmentsSub(supermod.Shipments):
    def __init__(self, Shipment=None):
        super(ShipmentsSub, self).__init__(Shipment, )
supermod.Shipments.subclass = ShipmentsSub
# end class ShipmentsSub


class ShipmentSub(supermod.Shipment):
    def __init__(self, Meta=None, Header=None, ContainerLevel=None, OrderLevel=None, PackLevel=None, ItemLevel=None, Summary=None):
        super(ShipmentSub, self).__init__(Meta, Header, ContainerLevel, OrderLevel, PackLevel, ItemLevel, Summary, )
supermod.Shipment.subclass = ShipmentSub
# end class ShipmentSub


class ContainerLevelSub(supermod.ContainerLevel):
    def __init__(self, Container=None, Date=None, Reference=None, Notes=None, QuantityAndWeight=None, CarrierInformation=None, Address=None, OrderLevel=None, PackLevel=None, ItemLevel=None):
        super(ContainerLevelSub, self).__init__(Container, Date, Reference, Notes, QuantityAndWeight, CarrierInformation, Address, OrderLevel, PackLevel, ItemLevel, )
supermod.ContainerLevel.subclass = ContainerLevelSub
# end class ContainerLevelSub


class OrderLevelSub(supermod.OrderLevel):
    def __init__(self, OrderHeader=None, QuantityAndWeight=None, CarrierInformation=None, Date=None, Reference=None, Notes=None, Address=None, Tax=None, ChargesAllowances=None, Commodity=None, PackLevel=None, ItemLevel=None, ContainerLevel=None):
        super(OrderLevelSub, self).__init__(OrderHeader, QuantityAndWeight, CarrierInformation, Date, Reference, Notes, Address, Tax, ChargesAllowances, Commodity, PackLevel, ItemLevel, ContainerLevel, )
supermod.OrderLevel.subclass = OrderLevelSub
# end class OrderLevelSub


class PackLevelSub(supermod.PackLevel):
    def __init__(self, Pack=None, PhysicalDetails=None, MarksAndNumbersCollection=None, PalletInformation=None, Date=None, Reference=None, Notes=None, Address=None, Tax=None, ChargesAllowances=None, CarrierInformation=None, Packaging=None, ItemLevel=None, PackLevel_member=None):
        super(PackLevelSub, self).__init__(Pack, PhysicalDetails, MarksAndNumbersCollection, PalletInformation, Date, Reference, Notes, Address, Tax, ChargesAllowances, CarrierInformation, Packaging, ItemLevel, PackLevel_member, )
supermod.PackLevel.subclass = PackLevelSub
# end class PackLevelSub


class ItemLevelSub(supermod.ItemLevel):
    def __init__(self, ShipmentLine=None, PhysicalDetails=None, CarrierSpecialHandlingDetail=None, CarrierInformation=None, Measurements=None, PriceInformation=None, ProductOrItemDescription=None, MasterItemAttribute=None, Date=None, Reference=None, Notes=None, Commodity=None, Address=None, Sublines=None, Tax=None, ChargesAllowances=None, ItemLoadInfo=None, PackLevel=None, OrderLevel=None):
        super(ItemLevelSub, self).__init__(ShipmentLine, PhysicalDetails, CarrierSpecialHandlingDetail, CarrierInformation, Measurements, PriceInformation, ProductOrItemDescription, MasterItemAttribute, Date, Reference, Notes, Commodity, Address, Sublines, Tax, ChargesAllowances, ItemLoadInfo, PackLevel, OrderLevel, )
supermod.ItemLevel.subclass = ItemLevelSub
# end class ItemLevelSub


class attributes_stringSub(supermod.attributes_string):
    def __init__(self, not_equal=None, requires_others=None, score=None, qualified_rep=None, requires_one=None, valueOf_=None):
        super(attributes_stringSub, self).__init__(not_equal, requires_others, score, qualified_rep, requires_one, valueOf_, )
supermod.attributes_string.subclass = attributes_stringSub
# end class attributes_stringSub


class MetaTypeSub(supermod.MetaType):
    def __init__(self, SenderUniqueID=None, SenderCompanyName=None, ReceiverUniqueID=None, ReceiverCompanyName=None, IsDropShip=None, InterchangeControlNumber=None, GroupControlIdentifier=None, GroupControlNumber=None, DocumentControlIdentifier=None, DocumentControlNumber=None, InterchangeSenderID=None, InterchangeReceiverID=None, GroupSenderID=None, GroupReceiverID=None, BatchPart=None, BatchTotal=None, BatchID=None, Comments=None, Validation=None, OrderManagement=None, Version=None):
        super(MetaTypeSub, self).__init__(SenderUniqueID, SenderCompanyName, ReceiverUniqueID, ReceiverCompanyName, IsDropShip, InterchangeControlNumber, GroupControlIdentifier, GroupControlNumber, DocumentControlIdentifier, DocumentControlNumber, InterchangeSenderID, InterchangeReceiverID, GroupSenderID, GroupReceiverID, BatchPart, BatchTotal, BatchID, Comments, Validation, OrderManagement, Version, )
supermod.MetaType.subclass = MetaTypeSub
# end class MetaTypeSub


class HeaderTypeSub(supermod.HeaderType):
    def __init__(self, ShipmentHeader=None, Date=None, Reference=None, Notes=None, Contact=None, Address=None, CarrierInformation=None, QuantityAndWeight=None, CarrierSpecialHandlingDetail=None, Tax=None, ChargesAllowances=None, FOBRelatedInstruction=None):
        super(HeaderTypeSub, self).__init__(ShipmentHeader, Date, Reference, Notes, Contact, Address, CarrierInformation, QuantityAndWeight, CarrierSpecialHandlingDetail, Tax, ChargesAllowances, FOBRelatedInstruction, )
supermod.HeaderType.subclass = HeaderTypeSub
# end class HeaderTypeSub


class ShipmentHeaderTypeSub(supermod.ShipmentHeaderType):
    def __init__(self, TradingPartnerId=None, ShipmentIdentification=None, ShipDate=None, ShipmentTime=None, TsetPurposeCode=None, TsetTypeCode=None, ShipNoticeDate=None, ShipNoticeTime=None, ASNStructureCode=None, FairLaborCompliant=None, BuyersCurrency=None, SellersCurrency=None, ExchangeRate=None, StatusReasonCode=None, BillOfLadingNumber=None, CarrierProNumber=None, AppointmentNumber=None, PickupNumber=None, RequestedPickupDate=None, RequestedPickupTime=None, ScheduledShipDate=None, ScheduledShipTime=None, CurrentScheduledDeliveryDate=None, CurrentScheduledDeliveryTime=None, CurrentScheduledShipDate=None, CurrentScheduledShipTime=None, DocumentVersion=None, DocumentRevision=None):
        super(ShipmentHeaderTypeSub, self).__init__(TradingPartnerId, ShipmentIdentification, ShipDate, ShipmentTime, TsetPurposeCode, TsetTypeCode, ShipNoticeDate, ShipNoticeTime, ASNStructureCode, FairLaborCompliant, BuyersCurrency, SellersCurrency, ExchangeRate, StatusReasonCode, BillOfLadingNumber, CarrierProNumber, AppointmentNumber, PickupNumber, RequestedPickupDate, RequestedPickupTime, ScheduledShipDate, ScheduledShipTime, CurrentScheduledDeliveryDate, CurrentScheduledDeliveryTime, CurrentScheduledShipDate, CurrentScheduledShipTime, DocumentVersion, DocumentRevision, )
supermod.ShipmentHeaderType.subclass = ShipmentHeaderTypeSub
# end class ShipmentHeaderTypeSub


class DateTypeSub(supermod.DateType):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateTypeSub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType.subclass = DateTypeSub
# end class DateTypeSub


class ReferenceTypeSub(supermod.ReferenceType):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceTypeSub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType.subclass = ReferenceTypeSub
# end class ReferenceTypeSub


class ReferenceIDsTypeSub(supermod.ReferenceIDsType):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsTypeSub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType.subclass = ReferenceIDsTypeSub
# end class ReferenceIDsTypeSub


class NotesTypeSub(supermod.NotesType):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesTypeSub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType.subclass = NotesTypeSub
# end class NotesTypeSub


class ContactTypeSub(supermod.ContactType):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactTypeSub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType.subclass = ContactTypeSub
# end class ContactTypeSub


class AdditionalContactDetailsTypeSub(supermod.AdditionalContactDetailsType):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsTypeSub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType.subclass = AdditionalContactDetailsTypeSub
# end class AdditionalContactDetailsTypeSub


class AddressTypeSub(supermod.AddressType):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressTypeSub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType.subclass = AddressTypeSub
# end class AddressTypeSub


class ReferenceType1Sub(supermod.ReferenceType1):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType1Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType1.subclass = ReferenceType1Sub
# end class ReferenceType1Sub


class ReferenceIDsType2Sub(supermod.ReferenceIDsType2):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType2Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType2.subclass = ReferenceIDsType2Sub
# end class ReferenceIDsType2Sub


class ContactType3Sub(supermod.ContactType3):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType3Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType3.subclass = ContactType3Sub
# end class ContactType3Sub


class AdditionalContactDetailsType4Sub(supermod.AdditionalContactDetailsType4):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType4Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType4.subclass = AdditionalContactDetailsType4Sub
# end class AdditionalContactDetailsType4Sub


class DateType5Sub(supermod.DateType5):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType5Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType5.subclass = DateType5Sub
# end class DateType5Sub


class CarrierInformationTypeSub(supermod.CarrierInformationType):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationTypeSub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType.subclass = CarrierInformationTypeSub
# end class CarrierInformationTypeSub


class ServiceLevelCodesTypeSub(supermod.ServiceLevelCodesType):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesTypeSub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType.subclass = ServiceLevelCodesTypeSub
# end class ServiceLevelCodesTypeSub


class AddressType6Sub(supermod.AddressType6):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType6Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType6.subclass = AddressType6Sub
# end class AddressType6Sub


class DateType7Sub(supermod.DateType7):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType7Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType7.subclass = DateType7Sub
# end class DateType7Sub


class QuantityAndWeightTypeSub(supermod.QuantityAndWeightType):
    def __init__(self, PackingMedium=None, PackingMaterial=None, LadingQuantity=None, LadingDescription=None, WeightQualifier=None, Weight=None, WeightUOM=None, Volume=None, VolumeUOM=None, PalletExchangeCode=None):
        super(QuantityAndWeightTypeSub, self).__init__(PackingMedium, PackingMaterial, LadingQuantity, LadingDescription, WeightQualifier, Weight, WeightUOM, Volume, VolumeUOM, PalletExchangeCode, )
supermod.QuantityAndWeightType.subclass = QuantityAndWeightTypeSub
# end class QuantityAndWeightTypeSub


class CarrierSpecialHandlingDetailTypeSub(supermod.CarrierSpecialHandlingDetailType):
    def __init__(self, SpecialHandlingCode=None, HazardousMaterialCode=None, HazardousMaterialClass=None, Description=None, YesOrNoResponse=None):
        super(CarrierSpecialHandlingDetailTypeSub, self).__init__(SpecialHandlingCode, HazardousMaterialCode, HazardousMaterialClass, Description, YesOrNoResponse, )
supermod.CarrierSpecialHandlingDetailType.subclass = CarrierSpecialHandlingDetailTypeSub
# end class CarrierSpecialHandlingDetailTypeSub


class TaxTypeSub(supermod.TaxType):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxTypeSub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType.subclass = TaxTypeSub
# end class TaxTypeSub


class ChargesAllowancesTypeSub(supermod.ChargesAllowancesType):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, Tax=None):
        super(ChargesAllowancesTypeSub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, Tax, )
supermod.ChargesAllowancesType.subclass = ChargesAllowancesTypeSub
# end class ChargesAllowancesTypeSub


class TaxType8Sub(supermod.TaxType8):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType8Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType8.subclass = TaxType8Sub
# end class TaxType8Sub


class FOBRelatedInstructionTypeSub(supermod.FOBRelatedInstructionType):
    def __init__(self, FOBPayCode=None, FOBLocationQualifier=None, FOBLocationDescription=None, FOBTitlePassageCode=None, FOBTitlePassageLocation=None, TransportationTermsQualifierCode=None, TransportationTermsCode=None, RiskOfLossCode=None, Description=None):
        super(FOBRelatedInstructionTypeSub, self).__init__(FOBPayCode, FOBLocationQualifier, FOBLocationDescription, FOBTitlePassageCode, FOBTitlePassageLocation, TransportationTermsQualifierCode, TransportationTermsCode, RiskOfLossCode, Description, )
supermod.FOBRelatedInstructionType.subclass = FOBRelatedInstructionTypeSub
# end class FOBRelatedInstructionTypeSub


class OrderLevelTypeSub(supermod.OrderLevelType):
    def __init__(self, OrderHeader=None, QuantityAndWeight=None, CarrierInformation=None, Date=None, Reference=None, Notes=None, Address=None, Tax=None, ChargesAllowances=None, Commodity=None, PackLevel=None, ItemLevel=None, ContainerLevel=None):
        super(OrderLevelTypeSub, self).__init__(OrderHeader, QuantityAndWeight, CarrierInformation, Date, Reference, Notes, Address, Tax, ChargesAllowances, Commodity, PackLevel, ItemLevel, ContainerLevel, )
supermod.OrderLevelType.subclass = OrderLevelTypeSub
# end class OrderLevelTypeSub


class OrderHeaderTypeSub(supermod.OrderHeaderType):
    def __init__(self, DepositorOrderNumber=None, InternalOrderNumber=None, InternalOrderDate=None, InvoiceNumber=None, InvoiceDate=None, PurchaseOrderNumber=None, ReleaseNumber=None, PurchaseOrderDate=None, Department=None, DepartmentDescription=None, Vendor=None, JobNumber=None, Division=None, CustomerAccountNumber=None, CustomerOrderNumber=None, PromotionDealNumber=None, PromotionDealDescription=None, DeliveryDate=None, DeliveryTime=None):
        super(OrderHeaderTypeSub, self).__init__(DepositorOrderNumber, InternalOrderNumber, InternalOrderDate, InvoiceNumber, InvoiceDate, PurchaseOrderNumber, ReleaseNumber, PurchaseOrderDate, Department, DepartmentDescription, Vendor, JobNumber, Division, CustomerAccountNumber, CustomerOrderNumber, PromotionDealNumber, PromotionDealDescription, DeliveryDate, DeliveryTime, )
supermod.OrderHeaderType.subclass = OrderHeaderTypeSub
# end class OrderHeaderTypeSub


class QuantityAndWeightType9Sub(supermod.QuantityAndWeightType9):
    def __init__(self, PackingMedium=None, PackingMaterial=None, LadingQuantity=None, LadingDescription=None, WeightQualifier=None, Weight=None, WeightUOM=None, Volume=None, VolumeUOM=None, PalletExchangeCode=None):
        super(QuantityAndWeightType9Sub, self).__init__(PackingMedium, PackingMaterial, LadingQuantity, LadingDescription, WeightQualifier, Weight, WeightUOM, Volume, VolumeUOM, PalletExchangeCode, )
supermod.QuantityAndWeightType9.subclass = QuantityAndWeightType9Sub
# end class QuantityAndWeightType9Sub


class CarrierInformationType10Sub(supermod.CarrierInformationType10):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationType10Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType10.subclass = CarrierInformationType10Sub
# end class CarrierInformationType10Sub


class ServiceLevelCodesType11Sub(supermod.ServiceLevelCodesType11):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType11Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType11.subclass = ServiceLevelCodesType11Sub
# end class ServiceLevelCodesType11Sub


class AddressType12Sub(supermod.AddressType12):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType12Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType12.subclass = AddressType12Sub
# end class AddressType12Sub


class DateType13Sub(supermod.DateType13):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType13Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType13.subclass = DateType13Sub
# end class DateType13Sub


class DateType14Sub(supermod.DateType14):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType14Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType14.subclass = DateType14Sub
# end class DateType14Sub


class ReferenceType15Sub(supermod.ReferenceType15):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType15Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType15.subclass = ReferenceType15Sub
# end class ReferenceType15Sub


class ReferenceIDsType16Sub(supermod.ReferenceIDsType16):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType16Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType16.subclass = ReferenceIDsType16Sub
# end class ReferenceIDsType16Sub


class NotesType17Sub(supermod.NotesType17):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType17Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType17.subclass = NotesType17Sub
# end class NotesType17Sub


class AddressType18Sub(supermod.AddressType18):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressType18Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType18.subclass = AddressType18Sub
# end class AddressType18Sub


class ReferenceType19Sub(supermod.ReferenceType19):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType19Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType19.subclass = ReferenceType19Sub
# end class ReferenceType19Sub


class ReferenceIDsType20Sub(supermod.ReferenceIDsType20):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType20Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType20.subclass = ReferenceIDsType20Sub
# end class ReferenceIDsType20Sub


class ContactType21Sub(supermod.ContactType21):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType21Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType21.subclass = ContactType21Sub
# end class ContactType21Sub


class AdditionalContactDetailsType22Sub(supermod.AdditionalContactDetailsType22):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType22Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType22.subclass = AdditionalContactDetailsType22Sub
# end class AdditionalContactDetailsType22Sub


class DateType23Sub(supermod.DateType23):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType23Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType23.subclass = DateType23Sub
# end class DateType23Sub


class TaxType24Sub(supermod.TaxType24):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType24Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType24.subclass = TaxType24Sub
# end class TaxType24Sub


class ChargesAllowancesType25Sub(supermod.ChargesAllowancesType25):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, Tax=None):
        super(ChargesAllowancesType25Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, Tax, )
supermod.ChargesAllowancesType25.subclass = ChargesAllowancesType25Sub
# end class ChargesAllowancesType25Sub


class TaxType26Sub(supermod.TaxType26):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType26Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType26.subclass = TaxType26Sub
# end class TaxType26Sub


class CommodityTypeSub(supermod.CommodityType):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityTypeSub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType.subclass = CommodityTypeSub
# end class CommodityTypeSub


class PackLevelTypeSub(supermod.PackLevelType):
    def __init__(self, Pack=None, PhysicalDetails=None, MarksAndNumbersCollection=None, PalletInformation=None, Date=None, Reference=None, Notes=None, Address=None, Tax=None, ChargesAllowances=None, CarrierInformation=None, Packaging=None, ItemLevel=None, PackLevel=None):
        super(PackLevelTypeSub, self).__init__(Pack, PhysicalDetails, MarksAndNumbersCollection, PalletInformation, Date, Reference, Notes, Address, Tax, ChargesAllowances, CarrierInformation, Packaging, ItemLevel, PackLevel, )
supermod.PackLevelType.subclass = PackLevelTypeSub
# end class PackLevelTypeSub


class PackTypeSub(supermod.PackType):
    def __init__(self, PackLevelType=None, ShippingSerialID=None, CarrierPackageID=None):
        super(PackTypeSub, self).__init__(PackLevelType, ShippingSerialID, CarrierPackageID, )
supermod.PackType.subclass = PackTypeSub
# end class PackTypeSub


class PhysicalDetailsTypeSub(supermod.PhysicalDetailsType):
    def __init__(self, PackQualifier=None, PackValue=None, PackSize=None, PackUOM=None, PackingMedium=None, PackingMaterial=None, WeightQualifier=None, PackWeight=None, PackWeightUOM=None, PackVolume=None, PackVolumeUOM=None, PackLength=None, PackWidth=None, PackHeight=None, PackDimensionUOM=None, Description=None, SurfaceLayerPositionCode=None, AssignedID=None):
        super(PhysicalDetailsTypeSub, self).__init__(PackQualifier, PackValue, PackSize, PackUOM, PackingMedium, PackingMaterial, WeightQualifier, PackWeight, PackWeightUOM, PackVolume, PackVolumeUOM, PackLength, PackWidth, PackHeight, PackDimensionUOM, Description, SurfaceLayerPositionCode, AssignedID, )
supermod.PhysicalDetailsType.subclass = PhysicalDetailsTypeSub
# end class PhysicalDetailsTypeSub


class MarksAndNumbersCollectionTypeSub(supermod.MarksAndNumbersCollectionType):
    def __init__(self, MarksAndNumbersQualifier1=None, MarksAndNumbers1=None):
        super(MarksAndNumbersCollectionTypeSub, self).__init__(MarksAndNumbersQualifier1, MarksAndNumbers1, )
supermod.MarksAndNumbersCollectionType.subclass = MarksAndNumbersCollectionTypeSub
# end class MarksAndNumbersCollectionTypeSub


class PalletInformationTypeSub(supermod.PalletInformationType):
    def __init__(self, PalletQualifier=None, PalletValue=None, PalletTypeCode=None, PalletTiers=None, PalletBlocks=None, UnitWeight=None, UnitWeightUOM=None, Length=None, Width=None, Height=None, UnitOfMeasure=None, WeightQualifier=None, PalletWeight=None, PalletWeightUOM=None, PalletVolume=None, PalletVolumeUOM=None, PalletExchangeCode=None, PalletStructureCode=None):
        super(PalletInformationTypeSub, self).__init__(PalletQualifier, PalletValue, PalletTypeCode, PalletTiers, PalletBlocks, UnitWeight, UnitWeightUOM, Length, Width, Height, UnitOfMeasure, WeightQualifier, PalletWeight, PalletWeightUOM, PalletVolume, PalletVolumeUOM, PalletExchangeCode, PalletStructureCode, )
supermod.PalletInformationType.subclass = PalletInformationTypeSub
# end class PalletInformationTypeSub


class DateType27Sub(supermod.DateType27):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType27Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType27.subclass = DateType27Sub
# end class DateType27Sub


class ReferenceType28Sub(supermod.ReferenceType28):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType28Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType28.subclass = ReferenceType28Sub
# end class ReferenceType28Sub


class ReferenceIDsType29Sub(supermod.ReferenceIDsType29):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType29Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType29.subclass = ReferenceIDsType29Sub
# end class ReferenceIDsType29Sub


class NotesType30Sub(supermod.NotesType30):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType30Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType30.subclass = NotesType30Sub
# end class NotesType30Sub


class AddressType31Sub(supermod.AddressType31):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressType31Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType31.subclass = AddressType31Sub
# end class AddressType31Sub


class ReferenceType32Sub(supermod.ReferenceType32):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType32Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType32.subclass = ReferenceType32Sub
# end class ReferenceType32Sub


class ReferenceIDsType33Sub(supermod.ReferenceIDsType33):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType33Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType33.subclass = ReferenceIDsType33Sub
# end class ReferenceIDsType33Sub


class ContactType34Sub(supermod.ContactType34):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType34Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType34.subclass = ContactType34Sub
# end class ContactType34Sub


class AdditionalContactDetailsType35Sub(supermod.AdditionalContactDetailsType35):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType35Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType35.subclass = AdditionalContactDetailsType35Sub
# end class AdditionalContactDetailsType35Sub


class DateType36Sub(supermod.DateType36):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType36Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType36.subclass = DateType36Sub
# end class DateType36Sub


class TaxType37Sub(supermod.TaxType37):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType37Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType37.subclass = TaxType37Sub
# end class TaxType37Sub


class ChargesAllowancesType38Sub(supermod.ChargesAllowancesType38):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, Tax=None):
        super(ChargesAllowancesType38Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, Tax, )
supermod.ChargesAllowancesType38.subclass = ChargesAllowancesType38Sub
# end class ChargesAllowancesType38Sub


class TaxType39Sub(supermod.TaxType39):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType39Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType39.subclass = TaxType39Sub
# end class TaxType39Sub


class CarrierInformationType40Sub(supermod.CarrierInformationType40):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationType40Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType40.subclass = CarrierInformationType40Sub
# end class CarrierInformationType40Sub


class ServiceLevelCodesType41Sub(supermod.ServiceLevelCodesType41):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType41Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType41.subclass = ServiceLevelCodesType41Sub
# end class ServiceLevelCodesType41Sub


class AddressType42Sub(supermod.AddressType42):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType42Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType42.subclass = AddressType42Sub
# end class AddressType42Sub


class DateType43Sub(supermod.DateType43):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType43Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType43.subclass = DateType43Sub
# end class DateType43Sub


class PackagingTypeSub(supermod.PackagingType):
    def __init__(self, ItemDescriptionType=None, PackagingCharacteristicCode=None, AgencyQualifierCode=None, PackagingDescriptionCode=None, PackagingDescription=None, UnitLoadOptionCode=None):
        super(PackagingTypeSub, self).__init__(ItemDescriptionType, PackagingCharacteristicCode, AgencyQualifierCode, PackagingDescriptionCode, PackagingDescription, UnitLoadOptionCode, )
supermod.PackagingType.subclass = PackagingTypeSub
# end class PackagingTypeSub


class ItemLevelTypeSub(supermod.ItemLevelType):
    def __init__(self, ShipmentLine=None, PhysicalDetails=None, CarrierSpecialHandlingDetail=None, CarrierInformation=None, Measurements=None, PriceInformation=None, ProductOrItemDescription=None, MasterItemAttribute=None, Date=None, Reference=None, Notes=None, Commodity=None, Address=None, Sublines=None, Tax=None, ChargesAllowances=None, ItemLoadInfo=None, PackLevel=None):
        super(ItemLevelTypeSub, self).__init__(ShipmentLine, PhysicalDetails, CarrierSpecialHandlingDetail, CarrierInformation, Measurements, PriceInformation, ProductOrItemDescription, MasterItemAttribute, Date, Reference, Notes, Commodity, Address, Sublines, Tax, ChargesAllowances, ItemLoadInfo, PackLevel, )
supermod.ItemLevelType.subclass = ItemLevelTypeSub
# end class ItemLevelTypeSub


class ShipmentLineTypeSub(supermod.ShipmentLineType):
    def __init__(self, LineSequenceNumber=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None, OrderQty=None, OrderQtyUOM=None, PurchasePriceType=None, PurchasePrice=None, PurchasePriceBasis=None, ItemStatusCode=None, ShipQty=None, ShipQtyUOM=None, ShipDate=None, QtyLeftToReceive=None, ProductSizeCode=None, ProductSizeDescription=None, ProductColorCode=None, ProductColorDescription=None, ProductMaterialCode=None, ProductMaterialDescription=None, ProductProcessCode=None, ProductProcessDescription=None, Department=None, DepartmentDescription=None, Class=None, SellerDateCode=None, NRFStandardColorAndSize=None):
        super(ShipmentLineTypeSub, self).__init__(LineSequenceNumber, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, OrderQty, OrderQtyUOM, PurchasePriceType, PurchasePrice, PurchasePriceBasis, ItemStatusCode, ShipQty, ShipQtyUOM, ShipDate, QtyLeftToReceive, ProductSizeCode, ProductSizeDescription, ProductColorCode, ProductColorDescription, ProductMaterialCode, ProductMaterialDescription, ProductProcessCode, ProductProcessDescription, Department, DepartmentDescription, Class, SellerDateCode, NRFStandardColorAndSize, )
supermod.ShipmentLineType.subclass = ShipmentLineTypeSub
# end class ShipmentLineTypeSub


class ProductIDTypeSub(supermod.ProductIDType):
    def __init__(self, PartNumberQual=None, PartNumber=None):
        super(ProductIDTypeSub, self).__init__(PartNumberQual, PartNumber, )
supermod.ProductIDType.subclass = ProductIDTypeSub
# end class ProductIDTypeSub


class NRFStandardColorAndSizeTypeSub(supermod.NRFStandardColorAndSizeType):
    def __init__(self, NRFColorCode=None, ColorCategoryName=None, ColorPrimaryDescription=None, NRFSizeCode=None, SizeCategoryName=None, SizePrimaryDescription=None, SizeSecondaryDescription=None, SizeTableName=None, SizeHeading1=None, SizeHeading2=None, SizeHeading3=None, SizeHeading4=None):
        super(NRFStandardColorAndSizeTypeSub, self).__init__(NRFColorCode, ColorCategoryName, ColorPrimaryDescription, NRFSizeCode, SizeCategoryName, SizePrimaryDescription, SizeSecondaryDescription, SizeTableName, SizeHeading1, SizeHeading2, SizeHeading3, SizeHeading4, )
supermod.NRFStandardColorAndSizeType.subclass = NRFStandardColorAndSizeTypeSub
# end class NRFStandardColorAndSizeTypeSub


class PhysicalDetailsType44Sub(supermod.PhysicalDetailsType44):
    def __init__(self, PackQualifier=None, PackValue=None, PackSize=None, PackUOM=None, PackingMedium=None, PackingMaterial=None, WeightQualifier=None, PackWeight=None, PackWeightUOM=None, PackVolume=None, PackVolumeUOM=None, PackLength=None, PackWidth=None, PackHeight=None, PackDimensionUOM=None, Description=None, SurfaceLayerPositionCode=None, AssignedID=None):
        super(PhysicalDetailsType44Sub, self).__init__(PackQualifier, PackValue, PackSize, PackUOM, PackingMedium, PackingMaterial, WeightQualifier, PackWeight, PackWeightUOM, PackVolume, PackVolumeUOM, PackLength, PackWidth, PackHeight, PackDimensionUOM, Description, SurfaceLayerPositionCode, AssignedID, )
supermod.PhysicalDetailsType44.subclass = PhysicalDetailsType44Sub
# end class PhysicalDetailsType44Sub


class CarrierSpecialHandlingDetailType45Sub(supermod.CarrierSpecialHandlingDetailType45):
    def __init__(self, SpecialHandlingCode=None, HazardousMaterialCode=None, HazardousMaterialClass=None, Description=None, YesOrNoResponse=None):
        super(CarrierSpecialHandlingDetailType45Sub, self).__init__(SpecialHandlingCode, HazardousMaterialCode, HazardousMaterialClass, Description, YesOrNoResponse, )
supermod.CarrierSpecialHandlingDetailType45.subclass = CarrierSpecialHandlingDetailType45Sub
# end class CarrierSpecialHandlingDetailType45Sub


class CarrierInformationType46Sub(supermod.CarrierInformationType46):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationType46Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType46.subclass = CarrierInformationType46Sub
# end class CarrierInformationType46Sub


class ServiceLevelCodesType47Sub(supermod.ServiceLevelCodesType47):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType47Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType47.subclass = ServiceLevelCodesType47Sub
# end class ServiceLevelCodesType47Sub


class AddressType48Sub(supermod.AddressType48):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType48Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType48.subclass = AddressType48Sub
# end class AddressType48Sub


class DateType49Sub(supermod.DateType49):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType49Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType49.subclass = DateType49Sub
# end class DateType49Sub


class MeasurementsTypeSub(supermod.MeasurementsType):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsTypeSub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType.subclass = MeasurementsTypeSub
# end class MeasurementsTypeSub


class PriceInformationTypeSub(supermod.PriceInformationType):
    def __init__(self, ChangeReasonCode=None, EffectiveDate=None, PriceTypeIDCode=None, UnitPrice=None, UnitPriceBasis=None, Currency=None, PriceMultiplierQual=None, PriceMultiplier=None, RebateAmount=None, Quantity=None, QuantityUOM=None, MultiplePriceQuantity=None, ClassOfTradeCode=None, ConditionValue=None, Description=None):
        super(PriceInformationTypeSub, self).__init__(ChangeReasonCode, EffectiveDate, PriceTypeIDCode, UnitPrice, UnitPriceBasis, Currency, PriceMultiplierQual, PriceMultiplier, RebateAmount, Quantity, QuantityUOM, MultiplePriceQuantity, ClassOfTradeCode, ConditionValue, Description, )
supermod.PriceInformationType.subclass = PriceInformationTypeSub
# end class PriceInformationTypeSub


class ProductOrItemDescriptionTypeSub(supermod.ProductOrItemDescriptionType):
    def __init__(self, ItemDescriptionType=None, ProductCharacteristicCode=None, AgencyQualifierCode=None, ProductDescriptionCode=None, ProductDescription=None, SurfaceLayerPositionCode=None, SourceSubqualifier=None, YesOrNoResponse=None, LanguageCode=None):
        super(ProductOrItemDescriptionTypeSub, self).__init__(ItemDescriptionType, ProductCharacteristicCode, AgencyQualifierCode, ProductDescriptionCode, ProductDescription, SurfaceLayerPositionCode, SourceSubqualifier, YesOrNoResponse, LanguageCode, )
supermod.ProductOrItemDescriptionType.subclass = ProductOrItemDescriptionTypeSub
# end class ProductOrItemDescriptionTypeSub


class MasterItemAttributeTypeSub(supermod.MasterItemAttributeType):
    def __init__(self, ItemAttribute=None):
        super(MasterItemAttributeTypeSub, self).__init__(ItemAttribute, )
supermod.MasterItemAttributeType.subclass = MasterItemAttributeTypeSub
# end class MasterItemAttributeTypeSub


class ItemAttributeTypeSub(supermod.ItemAttributeType):
    def __init__(self, ItemAttributeQualifier=None, Value=None, ValueUOM=None, Description=None, YesOrNoResponse=None, Measurements=None):
        super(ItemAttributeTypeSub, self).__init__(ItemAttributeQualifier, Value, ValueUOM, Description, YesOrNoResponse, Measurements, )
supermod.ItemAttributeType.subclass = ItemAttributeTypeSub
# end class ItemAttributeTypeSub


class MeasurementsType50Sub(supermod.MeasurementsType50):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType50Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType50.subclass = MeasurementsType50Sub
# end class MeasurementsType50Sub


class DateType51Sub(supermod.DateType51):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType51Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType51.subclass = DateType51Sub
# end class DateType51Sub


class ReferenceType52Sub(supermod.ReferenceType52):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType52Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType52.subclass = ReferenceType52Sub
# end class ReferenceType52Sub


class ReferenceIDsType53Sub(supermod.ReferenceIDsType53):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType53Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType53.subclass = ReferenceIDsType53Sub
# end class ReferenceIDsType53Sub


class NotesType54Sub(supermod.NotesType54):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType54Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType54.subclass = NotesType54Sub
# end class NotesType54Sub


class CommodityType55Sub(supermod.CommodityType55):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType55Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType55.subclass = CommodityType55Sub
# end class CommodityType55Sub


class AddressType56Sub(supermod.AddressType56):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressType56Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType56.subclass = AddressType56Sub
# end class AddressType56Sub


class ReferenceType57Sub(supermod.ReferenceType57):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType57Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType57.subclass = ReferenceType57Sub
# end class ReferenceType57Sub


class ReferenceIDsType58Sub(supermod.ReferenceIDsType58):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType58Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType58.subclass = ReferenceIDsType58Sub
# end class ReferenceIDsType58Sub


class ContactType59Sub(supermod.ContactType59):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType59Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType59.subclass = ContactType59Sub
# end class ContactType59Sub


class AdditionalContactDetailsType60Sub(supermod.AdditionalContactDetailsType60):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType60Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType60.subclass = AdditionalContactDetailsType60Sub
# end class AdditionalContactDetailsType60Sub


class DateType61Sub(supermod.DateType61):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType61Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType61.subclass = DateType61Sub
# end class DateType61Sub


class SublinesTypeSub(supermod.SublinesType):
    def __init__(self, Subline=None):
        super(SublinesTypeSub, self).__init__(Subline, )
supermod.SublinesType.subclass = SublinesTypeSub
# end class SublinesTypeSub


class SublineTypeSub(supermod.SublineType):
    def __init__(self, SublineItemDetail=None, PriceInformation=None, ProductOrItemDescription=None, Commodity=None):
        super(SublineTypeSub, self).__init__(SublineItemDetail, PriceInformation, ProductOrItemDescription, Commodity, )
supermod.SublineType.subclass = SublineTypeSub
# end class SublineTypeSub


class SublineItemDetailTypeSub(supermod.SublineItemDetailType):
    def __init__(self, LineSequenceNumber=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None, ProductSizeCode=None, ProductSizeDescription=None, ProductColorCode=None, ProductColorDescription=None, ProductMaterialCode=None, ProductMaterialDescription=None, ProductProcessCode=None, ProductProcessDescription=None, QtyPer=None, QtyPerUOM=None, PurchasePriceType=None, PurchasePrice=None, PurchasePriceBasis=None, NRFStandardColorAndSize=None):
        super(SublineItemDetailTypeSub, self).__init__(LineSequenceNumber, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, ProductSizeCode, ProductSizeDescription, ProductColorCode, ProductColorDescription, ProductMaterialCode, ProductMaterialDescription, ProductProcessCode, ProductProcessDescription, QtyPer, QtyPerUOM, PurchasePriceType, PurchasePrice, PurchasePriceBasis, NRFStandardColorAndSize, )
supermod.SublineItemDetailType.subclass = SublineItemDetailTypeSub
# end class SublineItemDetailTypeSub


class ProductIDType62Sub(supermod.ProductIDType62):
    def __init__(self, PartNumberQual=None, PartNumber=None):
        super(ProductIDType62Sub, self).__init__(PartNumberQual, PartNumber, )
supermod.ProductIDType62.subclass = ProductIDType62Sub
# end class ProductIDType62Sub


class NRFStandardColorAndSizeType63Sub(supermod.NRFStandardColorAndSizeType63):
    def __init__(self, NRFColorCode=None, ColorCategoryName=None, ColorPrimaryDescription=None, NRFSizeCode=None, SizeCategoryName=None, SizePrimaryDescription=None, SizeSecondaryDescription=None, SizeTableName=None, SizeHeading1=None, SizeHeading2=None, SizeHeading3=None, SizeHeading4=None):
        super(NRFStandardColorAndSizeType63Sub, self).__init__(NRFColorCode, ColorCategoryName, ColorPrimaryDescription, NRFSizeCode, SizeCategoryName, SizePrimaryDescription, SizeSecondaryDescription, SizeTableName, SizeHeading1, SizeHeading2, SizeHeading3, SizeHeading4, )
supermod.NRFStandardColorAndSizeType63.subclass = NRFStandardColorAndSizeType63Sub
# end class NRFStandardColorAndSizeType63Sub


class PriceInformationType64Sub(supermod.PriceInformationType64):
    def __init__(self, ChangeReasonCode=None, EffectiveDate=None, PriceTypeIDCode=None, UnitPrice=None, UnitPriceBasis=None, Currency=None, PriceMultiplierQual=None, PriceMultiplier=None, RebateAmount=None, Quantity=None, QuantityUOM=None, MultiplePriceQuantity=None, ClassOfTradeCode=None, ConditionValue=None, Description=None):
        super(PriceInformationType64Sub, self).__init__(ChangeReasonCode, EffectiveDate, PriceTypeIDCode, UnitPrice, UnitPriceBasis, Currency, PriceMultiplierQual, PriceMultiplier, RebateAmount, Quantity, QuantityUOM, MultiplePriceQuantity, ClassOfTradeCode, ConditionValue, Description, )
supermod.PriceInformationType64.subclass = PriceInformationType64Sub
# end class PriceInformationType64Sub


class ProductOrItemDescriptionType65Sub(supermod.ProductOrItemDescriptionType65):
    def __init__(self, ItemDescriptionType=None, ProductCharacteristicCode=None, AgencyQualifierCode=None, ProductDescriptionCode=None, ProductDescription=None, SurfaceLayerPositionCode=None, SourceSubqualifier=None, YesOrNoResponse=None, LanguageCode=None):
        super(ProductOrItemDescriptionType65Sub, self).__init__(ItemDescriptionType, ProductCharacteristicCode, AgencyQualifierCode, ProductDescriptionCode, ProductDescription, SurfaceLayerPositionCode, SourceSubqualifier, YesOrNoResponse, LanguageCode, )
supermod.ProductOrItemDescriptionType65.subclass = ProductOrItemDescriptionType65Sub
# end class ProductOrItemDescriptionType65Sub


class CommodityType66Sub(supermod.CommodityType66):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType66Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType66.subclass = CommodityType66Sub
# end class CommodityType66Sub


class TaxType67Sub(supermod.TaxType67):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType67Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType67.subclass = TaxType67Sub
# end class TaxType67Sub


class ChargesAllowancesType68Sub(supermod.ChargesAllowancesType68):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, Tax=None):
        super(ChargesAllowancesType68Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, Tax, )
supermod.ChargesAllowancesType68.subclass = ChargesAllowancesType68Sub
# end class ChargesAllowancesType68Sub


class TaxType69Sub(supermod.TaxType69):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType69Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType69.subclass = TaxType69Sub
# end class TaxType69Sub


class ItemLoadInfoTypeSub(supermod.ItemLoadInfoType):
    def __init__(self, ItemLoad=None, Reference=None, Notes=None):
        super(ItemLoadInfoTypeSub, self).__init__(ItemLoad, Reference, Notes, )
supermod.ItemLoadInfoType.subclass = ItemLoadInfoTypeSub
# end class ItemLoadInfoTypeSub


class ItemLoadTypeSub(supermod.ItemLoadType):
    def __init__(self, NumberOfLoads=None, UnitsShipped=None, PackingMedium=None, PackingMaterial=None, LoadSize=None, LoadSizeUOM=None):
        super(ItemLoadTypeSub, self).__init__(NumberOfLoads, UnitsShipped, PackingMedium, PackingMaterial, LoadSize, LoadSizeUOM, )
supermod.ItemLoadType.subclass = ItemLoadTypeSub
# end class ItemLoadTypeSub


class ReferenceType70Sub(supermod.ReferenceType70):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType70Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType70.subclass = ReferenceType70Sub
# end class ReferenceType70Sub


class ReferenceIDsType71Sub(supermod.ReferenceIDsType71):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType71Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType71.subclass = ReferenceIDsType71Sub
# end class ReferenceIDsType71Sub


class NotesType72Sub(supermod.NotesType72):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType72Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType72.subclass = NotesType72Sub
# end class NotesType72Sub


class PackLevelType73Sub(supermod.PackLevelType73):
    def __init__(self, Pack=None, PhysicalDetails=None, MarksAndNumbersCollection=None, PalletInformation=None, Date=None, Reference=None, Notes=None, Address=None, Tax=None, ChargesAllowances=None, CarrierInformation=None, Packaging=None, ItemLevel=None):
        super(PackLevelType73Sub, self).__init__(Pack, PhysicalDetails, MarksAndNumbersCollection, PalletInformation, Date, Reference, Notes, Address, Tax, ChargesAllowances, CarrierInformation, Packaging, ItemLevel, )
supermod.PackLevelType73.subclass = PackLevelType73Sub
# end class PackLevelType73Sub


class PackType74Sub(supermod.PackType74):
    def __init__(self, PackLevelType=None, ShippingSerialID=None, CarrierPackageID=None):
        super(PackType74Sub, self).__init__(PackLevelType, ShippingSerialID, CarrierPackageID, )
supermod.PackType74.subclass = PackType74Sub
# end class PackType74Sub


class PhysicalDetailsType75Sub(supermod.PhysicalDetailsType75):
    def __init__(self, PackQualifier=None, PackValue=None, PackSize=None, PackUOM=None, PackingMedium=None, PackingMaterial=None, WeightQualifier=None, PackWeight=None, PackWeightUOM=None, PackVolume=None, PackVolumeUOM=None, PackLength=None, PackWidth=None, PackHeight=None, PackDimensionUOM=None, Description=None, SurfaceLayerPositionCode=None, AssignedID=None):
        super(PhysicalDetailsType75Sub, self).__init__(PackQualifier, PackValue, PackSize, PackUOM, PackingMedium, PackingMaterial, WeightQualifier, PackWeight, PackWeightUOM, PackVolume, PackVolumeUOM, PackLength, PackWidth, PackHeight, PackDimensionUOM, Description, SurfaceLayerPositionCode, AssignedID, )
supermod.PhysicalDetailsType75.subclass = PhysicalDetailsType75Sub
# end class PhysicalDetailsType75Sub


class MarksAndNumbersCollectionType76Sub(supermod.MarksAndNumbersCollectionType76):
    def __init__(self, MarksAndNumbersQualifier1=None, MarksAndNumbers1=None):
        super(MarksAndNumbersCollectionType76Sub, self).__init__(MarksAndNumbersQualifier1, MarksAndNumbers1, )
supermod.MarksAndNumbersCollectionType76.subclass = MarksAndNumbersCollectionType76Sub
# end class MarksAndNumbersCollectionType76Sub


class PalletInformationType77Sub(supermod.PalletInformationType77):
    def __init__(self, PalletQualifier=None, PalletValue=None, PalletTypeCode=None, PalletTiers=None, PalletBlocks=None, UnitWeight=None, UnitWeightUOM=None, Length=None, Width=None, Height=None, UnitOfMeasure=None, WeightQualifier=None, PalletWeight=None, PalletWeightUOM=None, PalletVolume=None, PalletVolumeUOM=None, PalletExchangeCode=None, PalletStructureCode=None):
        super(PalletInformationType77Sub, self).__init__(PalletQualifier, PalletValue, PalletTypeCode, PalletTiers, PalletBlocks, UnitWeight, UnitWeightUOM, Length, Width, Height, UnitOfMeasure, WeightQualifier, PalletWeight, PalletWeightUOM, PalletVolume, PalletVolumeUOM, PalletExchangeCode, PalletStructureCode, )
supermod.PalletInformationType77.subclass = PalletInformationType77Sub
# end class PalletInformationType77Sub


class DateType78Sub(supermod.DateType78):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType78Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType78.subclass = DateType78Sub
# end class DateType78Sub


class ReferenceType79Sub(supermod.ReferenceType79):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType79Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType79.subclass = ReferenceType79Sub
# end class ReferenceType79Sub


class ReferenceIDsType80Sub(supermod.ReferenceIDsType80):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType80Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType80.subclass = ReferenceIDsType80Sub
# end class ReferenceIDsType80Sub


class NotesType81Sub(supermod.NotesType81):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType81Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType81.subclass = NotesType81Sub
# end class NotesType81Sub


class AddressType82Sub(supermod.AddressType82):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressType82Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType82.subclass = AddressType82Sub
# end class AddressType82Sub


class ReferenceType83Sub(supermod.ReferenceType83):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType83Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType83.subclass = ReferenceType83Sub
# end class ReferenceType83Sub


class ReferenceIDsType84Sub(supermod.ReferenceIDsType84):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType84Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType84.subclass = ReferenceIDsType84Sub
# end class ReferenceIDsType84Sub


class ContactType85Sub(supermod.ContactType85):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType85Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType85.subclass = ContactType85Sub
# end class ContactType85Sub


class AdditionalContactDetailsType86Sub(supermod.AdditionalContactDetailsType86):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType86Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType86.subclass = AdditionalContactDetailsType86Sub
# end class AdditionalContactDetailsType86Sub


class DateType87Sub(supermod.DateType87):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType87Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType87.subclass = DateType87Sub
# end class DateType87Sub


class TaxType88Sub(supermod.TaxType88):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType88Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType88.subclass = TaxType88Sub
# end class TaxType88Sub


class ChargesAllowancesType89Sub(supermod.ChargesAllowancesType89):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, Tax=None):
        super(ChargesAllowancesType89Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, Tax, )
supermod.ChargesAllowancesType89.subclass = ChargesAllowancesType89Sub
# end class ChargesAllowancesType89Sub


class TaxType90Sub(supermod.TaxType90):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType90Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType90.subclass = TaxType90Sub
# end class TaxType90Sub


class CarrierInformationType91Sub(supermod.CarrierInformationType91):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationType91Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType91.subclass = CarrierInformationType91Sub
# end class CarrierInformationType91Sub


class ServiceLevelCodesType92Sub(supermod.ServiceLevelCodesType92):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType92Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType92.subclass = ServiceLevelCodesType92Sub
# end class ServiceLevelCodesType92Sub


class AddressType93Sub(supermod.AddressType93):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType93Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType93.subclass = AddressType93Sub
# end class AddressType93Sub


class DateType94Sub(supermod.DateType94):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType94Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType94.subclass = DateType94Sub
# end class DateType94Sub


class PackagingType95Sub(supermod.PackagingType95):
    def __init__(self, ItemDescriptionType=None, PackagingCharacteristicCode=None, AgencyQualifierCode=None, PackagingDescriptionCode=None, PackagingDescription=None, UnitLoadOptionCode=None):
        super(PackagingType95Sub, self).__init__(ItemDescriptionType, PackagingCharacteristicCode, AgencyQualifierCode, PackagingDescriptionCode, PackagingDescription, UnitLoadOptionCode, )
supermod.PackagingType95.subclass = PackagingType95Sub
# end class PackagingType95Sub


class ItemLevelType96Sub(supermod.ItemLevelType96):
    def __init__(self, ShipmentLine=None, PhysicalDetails=None, CarrierSpecialHandlingDetail=None, CarrierInformation=None, Measurements=None, PriceInformation=None, ProductOrItemDescription=None, MasterItemAttribute=None, Date=None, Reference=None, Notes=None, Commodity=None, Address=None, Sublines=None, Tax=None, ChargesAllowances=None, ItemLoadInfo=None):
        super(ItemLevelType96Sub, self).__init__(ShipmentLine, PhysicalDetails, CarrierSpecialHandlingDetail, CarrierInformation, Measurements, PriceInformation, ProductOrItemDescription, MasterItemAttribute, Date, Reference, Notes, Commodity, Address, Sublines, Tax, ChargesAllowances, ItemLoadInfo, )
supermod.ItemLevelType96.subclass = ItemLevelType96Sub
# end class ItemLevelType96Sub


class ShipmentLineType97Sub(supermod.ShipmentLineType97):
    def __init__(self, LineSequenceNumber=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None, OrderQty=None, OrderQtyUOM=None, PurchasePriceType=None, PurchasePrice=None, PurchasePriceBasis=None, ItemStatusCode=None, ShipQty=None, ShipQtyUOM=None, ShipDate=None, QtyLeftToReceive=None, ProductSizeCode=None, ProductSizeDescription=None, ProductColorCode=None, ProductColorDescription=None, ProductMaterialCode=None, ProductMaterialDescription=None, ProductProcessCode=None, ProductProcessDescription=None, Department=None, DepartmentDescription=None, Class=None, SellerDateCode=None, NRFStandardColorAndSize=None):
        super(ShipmentLineType97Sub, self).__init__(LineSequenceNumber, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, OrderQty, OrderQtyUOM, PurchasePriceType, PurchasePrice, PurchasePriceBasis, ItemStatusCode, ShipQty, ShipQtyUOM, ShipDate, QtyLeftToReceive, ProductSizeCode, ProductSizeDescription, ProductColorCode, ProductColorDescription, ProductMaterialCode, ProductMaterialDescription, ProductProcessCode, ProductProcessDescription, Department, DepartmentDescription, Class, SellerDateCode, NRFStandardColorAndSize, )
supermod.ShipmentLineType97.subclass = ShipmentLineType97Sub
# end class ShipmentLineType97Sub


class ProductIDType98Sub(supermod.ProductIDType98):
    def __init__(self, PartNumberQual=None, PartNumber=None):
        super(ProductIDType98Sub, self).__init__(PartNumberQual, PartNumber, )
supermod.ProductIDType98.subclass = ProductIDType98Sub
# end class ProductIDType98Sub


class NRFStandardColorAndSizeType99Sub(supermod.NRFStandardColorAndSizeType99):
    def __init__(self, NRFColorCode=None, ColorCategoryName=None, ColorPrimaryDescription=None, NRFSizeCode=None, SizeCategoryName=None, SizePrimaryDescription=None, SizeSecondaryDescription=None, SizeTableName=None, SizeHeading1=None, SizeHeading2=None, SizeHeading3=None, SizeHeading4=None):
        super(NRFStandardColorAndSizeType99Sub, self).__init__(NRFColorCode, ColorCategoryName, ColorPrimaryDescription, NRFSizeCode, SizeCategoryName, SizePrimaryDescription, SizeSecondaryDescription, SizeTableName, SizeHeading1, SizeHeading2, SizeHeading3, SizeHeading4, )
supermod.NRFStandardColorAndSizeType99.subclass = NRFStandardColorAndSizeType99Sub
# end class NRFStandardColorAndSizeType99Sub


class PhysicalDetailsType100Sub(supermod.PhysicalDetailsType100):
    def __init__(self, PackQualifier=None, PackValue=None, PackSize=None, PackUOM=None, PackingMedium=None, PackingMaterial=None, WeightQualifier=None, PackWeight=None, PackWeightUOM=None, PackVolume=None, PackVolumeUOM=None, PackLength=None, PackWidth=None, PackHeight=None, PackDimensionUOM=None, Description=None, SurfaceLayerPositionCode=None, AssignedID=None):
        super(PhysicalDetailsType100Sub, self).__init__(PackQualifier, PackValue, PackSize, PackUOM, PackingMedium, PackingMaterial, WeightQualifier, PackWeight, PackWeightUOM, PackVolume, PackVolumeUOM, PackLength, PackWidth, PackHeight, PackDimensionUOM, Description, SurfaceLayerPositionCode, AssignedID, )
supermod.PhysicalDetailsType100.subclass = PhysicalDetailsType100Sub
# end class PhysicalDetailsType100Sub


class CarrierSpecialHandlingDetailType101Sub(supermod.CarrierSpecialHandlingDetailType101):
    def __init__(self, SpecialHandlingCode=None, HazardousMaterialCode=None, HazardousMaterialClass=None, Description=None, YesOrNoResponse=None):
        super(CarrierSpecialHandlingDetailType101Sub, self).__init__(SpecialHandlingCode, HazardousMaterialCode, HazardousMaterialClass, Description, YesOrNoResponse, )
supermod.CarrierSpecialHandlingDetailType101.subclass = CarrierSpecialHandlingDetailType101Sub
# end class CarrierSpecialHandlingDetailType101Sub


class CarrierInformationType102Sub(supermod.CarrierInformationType102):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationType102Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType102.subclass = CarrierInformationType102Sub
# end class CarrierInformationType102Sub


class ServiceLevelCodesType103Sub(supermod.ServiceLevelCodesType103):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType103Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType103.subclass = ServiceLevelCodesType103Sub
# end class ServiceLevelCodesType103Sub


class AddressType104Sub(supermod.AddressType104):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType104Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType104.subclass = AddressType104Sub
# end class AddressType104Sub


class DateType105Sub(supermod.DateType105):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType105Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType105.subclass = DateType105Sub
# end class DateType105Sub


class MeasurementsType106Sub(supermod.MeasurementsType106):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType106Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType106.subclass = MeasurementsType106Sub
# end class MeasurementsType106Sub


class PriceInformationType107Sub(supermod.PriceInformationType107):
    def __init__(self, ChangeReasonCode=None, EffectiveDate=None, PriceTypeIDCode=None, UnitPrice=None, UnitPriceBasis=None, Currency=None, PriceMultiplierQual=None, PriceMultiplier=None, RebateAmount=None, Quantity=None, QuantityUOM=None, MultiplePriceQuantity=None, ClassOfTradeCode=None, ConditionValue=None, Description=None):
        super(PriceInformationType107Sub, self).__init__(ChangeReasonCode, EffectiveDate, PriceTypeIDCode, UnitPrice, UnitPriceBasis, Currency, PriceMultiplierQual, PriceMultiplier, RebateAmount, Quantity, QuantityUOM, MultiplePriceQuantity, ClassOfTradeCode, ConditionValue, Description, )
supermod.PriceInformationType107.subclass = PriceInformationType107Sub
# end class PriceInformationType107Sub


class ProductOrItemDescriptionType108Sub(supermod.ProductOrItemDescriptionType108):
    def __init__(self, ItemDescriptionType=None, ProductCharacteristicCode=None, AgencyQualifierCode=None, ProductDescriptionCode=None, ProductDescription=None, SurfaceLayerPositionCode=None, SourceSubqualifier=None, YesOrNoResponse=None, LanguageCode=None):
        super(ProductOrItemDescriptionType108Sub, self).__init__(ItemDescriptionType, ProductCharacteristicCode, AgencyQualifierCode, ProductDescriptionCode, ProductDescription, SurfaceLayerPositionCode, SourceSubqualifier, YesOrNoResponse, LanguageCode, )
supermod.ProductOrItemDescriptionType108.subclass = ProductOrItemDescriptionType108Sub
# end class ProductOrItemDescriptionType108Sub


class MasterItemAttributeType109Sub(supermod.MasterItemAttributeType109):
    def __init__(self, ItemAttribute=None):
        super(MasterItemAttributeType109Sub, self).__init__(ItemAttribute, )
supermod.MasterItemAttributeType109.subclass = MasterItemAttributeType109Sub
# end class MasterItemAttributeType109Sub


class ItemAttributeType110Sub(supermod.ItemAttributeType110):
    def __init__(self, ItemAttributeQualifier=None, Value=None, ValueUOM=None, Description=None, YesOrNoResponse=None, Measurements=None):
        super(ItemAttributeType110Sub, self).__init__(ItemAttributeQualifier, Value, ValueUOM, Description, YesOrNoResponse, Measurements, )
supermod.ItemAttributeType110.subclass = ItemAttributeType110Sub
# end class ItemAttributeType110Sub


class MeasurementsType111Sub(supermod.MeasurementsType111):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType111Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType111.subclass = MeasurementsType111Sub
# end class MeasurementsType111Sub


class DateType112Sub(supermod.DateType112):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType112Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType112.subclass = DateType112Sub
# end class DateType112Sub


class ReferenceType113Sub(supermod.ReferenceType113):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType113Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType113.subclass = ReferenceType113Sub
# end class ReferenceType113Sub


class ReferenceIDsType114Sub(supermod.ReferenceIDsType114):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType114Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType114.subclass = ReferenceIDsType114Sub
# end class ReferenceIDsType114Sub


class NotesType115Sub(supermod.NotesType115):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType115Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType115.subclass = NotesType115Sub
# end class NotesType115Sub


class CommodityType116Sub(supermod.CommodityType116):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType116Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType116.subclass = CommodityType116Sub
# end class CommodityType116Sub


class AddressType117Sub(supermod.AddressType117):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressType117Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType117.subclass = AddressType117Sub
# end class AddressType117Sub


class ReferenceType118Sub(supermod.ReferenceType118):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType118Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType118.subclass = ReferenceType118Sub
# end class ReferenceType118Sub


class ReferenceIDsType119Sub(supermod.ReferenceIDsType119):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType119Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType119.subclass = ReferenceIDsType119Sub
# end class ReferenceIDsType119Sub


class ContactType120Sub(supermod.ContactType120):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType120Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType120.subclass = ContactType120Sub
# end class ContactType120Sub


class AdditionalContactDetailsType121Sub(supermod.AdditionalContactDetailsType121):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType121Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType121.subclass = AdditionalContactDetailsType121Sub
# end class AdditionalContactDetailsType121Sub


class DateType122Sub(supermod.DateType122):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType122Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType122.subclass = DateType122Sub
# end class DateType122Sub


class SublinesType123Sub(supermod.SublinesType123):
    def __init__(self, Subline=None):
        super(SublinesType123Sub, self).__init__(Subline, )
supermod.SublinesType123.subclass = SublinesType123Sub
# end class SublinesType123Sub


class SublineType124Sub(supermod.SublineType124):
    def __init__(self, SublineItemDetail=None, PriceInformation=None, ProductOrItemDescription=None, Commodity=None):
        super(SublineType124Sub, self).__init__(SublineItemDetail, PriceInformation, ProductOrItemDescription, Commodity, )
supermod.SublineType124.subclass = SublineType124Sub
# end class SublineType124Sub


class SublineItemDetailType125Sub(supermod.SublineItemDetailType125):
    def __init__(self, LineSequenceNumber=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None, ProductSizeCode=None, ProductSizeDescription=None, ProductColorCode=None, ProductColorDescription=None, ProductMaterialCode=None, ProductMaterialDescription=None, ProductProcessCode=None, ProductProcessDescription=None, QtyPer=None, QtyPerUOM=None, PurchasePriceType=None, PurchasePrice=None, PurchasePriceBasis=None, NRFStandardColorAndSize=None):
        super(SublineItemDetailType125Sub, self).__init__(LineSequenceNumber, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, ProductSizeCode, ProductSizeDescription, ProductColorCode, ProductColorDescription, ProductMaterialCode, ProductMaterialDescription, ProductProcessCode, ProductProcessDescription, QtyPer, QtyPerUOM, PurchasePriceType, PurchasePrice, PurchasePriceBasis, NRFStandardColorAndSize, )
supermod.SublineItemDetailType125.subclass = SublineItemDetailType125Sub
# end class SublineItemDetailType125Sub


class ProductIDType126Sub(supermod.ProductIDType126):
    def __init__(self, PartNumberQual=None, PartNumber=None):
        super(ProductIDType126Sub, self).__init__(PartNumberQual, PartNumber, )
supermod.ProductIDType126.subclass = ProductIDType126Sub
# end class ProductIDType126Sub


class NRFStandardColorAndSizeType127Sub(supermod.NRFStandardColorAndSizeType127):
    def __init__(self, NRFColorCode=None, ColorCategoryName=None, ColorPrimaryDescription=None, NRFSizeCode=None, SizeCategoryName=None, SizePrimaryDescription=None, SizeSecondaryDescription=None, SizeTableName=None, SizeHeading1=None, SizeHeading2=None, SizeHeading3=None, SizeHeading4=None):
        super(NRFStandardColorAndSizeType127Sub, self).__init__(NRFColorCode, ColorCategoryName, ColorPrimaryDescription, NRFSizeCode, SizeCategoryName, SizePrimaryDescription, SizeSecondaryDescription, SizeTableName, SizeHeading1, SizeHeading2, SizeHeading3, SizeHeading4, )
supermod.NRFStandardColorAndSizeType127.subclass = NRFStandardColorAndSizeType127Sub
# end class NRFStandardColorAndSizeType127Sub


class PriceInformationType128Sub(supermod.PriceInformationType128):
    def __init__(self, ChangeReasonCode=None, EffectiveDate=None, PriceTypeIDCode=None, UnitPrice=None, UnitPriceBasis=None, Currency=None, PriceMultiplierQual=None, PriceMultiplier=None, RebateAmount=None, Quantity=None, QuantityUOM=None, MultiplePriceQuantity=None, ClassOfTradeCode=None, ConditionValue=None, Description=None):
        super(PriceInformationType128Sub, self).__init__(ChangeReasonCode, EffectiveDate, PriceTypeIDCode, UnitPrice, UnitPriceBasis, Currency, PriceMultiplierQual, PriceMultiplier, RebateAmount, Quantity, QuantityUOM, MultiplePriceQuantity, ClassOfTradeCode, ConditionValue, Description, )
supermod.PriceInformationType128.subclass = PriceInformationType128Sub
# end class PriceInformationType128Sub


class ProductOrItemDescriptionType129Sub(supermod.ProductOrItemDescriptionType129):
    def __init__(self, ItemDescriptionType=None, ProductCharacteristicCode=None, AgencyQualifierCode=None, ProductDescriptionCode=None, ProductDescription=None, SurfaceLayerPositionCode=None, SourceSubqualifier=None, YesOrNoResponse=None, LanguageCode=None):
        super(ProductOrItemDescriptionType129Sub, self).__init__(ItemDescriptionType, ProductCharacteristicCode, AgencyQualifierCode, ProductDescriptionCode, ProductDescription, SurfaceLayerPositionCode, SourceSubqualifier, YesOrNoResponse, LanguageCode, )
supermod.ProductOrItemDescriptionType129.subclass = ProductOrItemDescriptionType129Sub
# end class ProductOrItemDescriptionType129Sub


class CommodityType130Sub(supermod.CommodityType130):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType130Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType130.subclass = CommodityType130Sub
# end class CommodityType130Sub


class TaxType131Sub(supermod.TaxType131):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType131Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType131.subclass = TaxType131Sub
# end class TaxType131Sub


class ChargesAllowancesType132Sub(supermod.ChargesAllowancesType132):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, Tax=None):
        super(ChargesAllowancesType132Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, Tax, )
supermod.ChargesAllowancesType132.subclass = ChargesAllowancesType132Sub
# end class ChargesAllowancesType132Sub


class TaxType133Sub(supermod.TaxType133):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType133Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType133.subclass = TaxType133Sub
# end class TaxType133Sub


class ItemLoadInfoType134Sub(supermod.ItemLoadInfoType134):
    def __init__(self, ItemLoad=None, Reference=None, Notes=None):
        super(ItemLoadInfoType134Sub, self).__init__(ItemLoad, Reference, Notes, )
supermod.ItemLoadInfoType134.subclass = ItemLoadInfoType134Sub
# end class ItemLoadInfoType134Sub


class ItemLoadType135Sub(supermod.ItemLoadType135):
    def __init__(self, NumberOfLoads=None, UnitsShipped=None, PackingMedium=None, PackingMaterial=None, LoadSize=None, LoadSizeUOM=None):
        super(ItemLoadType135Sub, self).__init__(NumberOfLoads, UnitsShipped, PackingMedium, PackingMaterial, LoadSize, LoadSizeUOM, )
supermod.ItemLoadType135.subclass = ItemLoadType135Sub
# end class ItemLoadType135Sub


class ReferenceType136Sub(supermod.ReferenceType136):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType136Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType136.subclass = ReferenceType136Sub
# end class ReferenceType136Sub


class ReferenceIDsType137Sub(supermod.ReferenceIDsType137):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType137Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType137.subclass = ReferenceIDsType137Sub
# end class ReferenceIDsType137Sub


class NotesType138Sub(supermod.NotesType138):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType138Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType138.subclass = NotesType138Sub
# end class NotesType138Sub


class ItemLevelType139Sub(supermod.ItemLevelType139):
    def __init__(self, ShipmentLine=None, PhysicalDetails=None, CarrierSpecialHandlingDetail=None, CarrierInformation=None, Measurements=None, PriceInformation=None, ProductOrItemDescription=None, MasterItemAttribute=None, Date=None, Reference=None, Notes=None, Commodity=None, Address=None, Sublines=None, Tax=None, ChargesAllowances=None, ItemLoadInfo=None, PackLevel=None):
        super(ItemLevelType139Sub, self).__init__(ShipmentLine, PhysicalDetails, CarrierSpecialHandlingDetail, CarrierInformation, Measurements, PriceInformation, ProductOrItemDescription, MasterItemAttribute, Date, Reference, Notes, Commodity, Address, Sublines, Tax, ChargesAllowances, ItemLoadInfo, PackLevel, )
supermod.ItemLevelType139.subclass = ItemLevelType139Sub
# end class ItemLevelType139Sub


class ShipmentLineType140Sub(supermod.ShipmentLineType140):
    def __init__(self, LineSequenceNumber=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None, OrderQty=None, OrderQtyUOM=None, PurchasePriceType=None, PurchasePrice=None, PurchasePriceBasis=None, ItemStatusCode=None, ShipQty=None, ShipQtyUOM=None, ShipDate=None, QtyLeftToReceive=None, ProductSizeCode=None, ProductSizeDescription=None, ProductColorCode=None, ProductColorDescription=None, ProductMaterialCode=None, ProductMaterialDescription=None, ProductProcessCode=None, ProductProcessDescription=None, Department=None, DepartmentDescription=None, Class=None, SellerDateCode=None, NRFStandardColorAndSize=None):
        super(ShipmentLineType140Sub, self).__init__(LineSequenceNumber, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, OrderQty, OrderQtyUOM, PurchasePriceType, PurchasePrice, PurchasePriceBasis, ItemStatusCode, ShipQty, ShipQtyUOM, ShipDate, QtyLeftToReceive, ProductSizeCode, ProductSizeDescription, ProductColorCode, ProductColorDescription, ProductMaterialCode, ProductMaterialDescription, ProductProcessCode, ProductProcessDescription, Department, DepartmentDescription, Class, SellerDateCode, NRFStandardColorAndSize, )
supermod.ShipmentLineType140.subclass = ShipmentLineType140Sub
# end class ShipmentLineType140Sub


class ProductIDType141Sub(supermod.ProductIDType141):
    def __init__(self, PartNumberQual=None, PartNumber=None):
        super(ProductIDType141Sub, self).__init__(PartNumberQual, PartNumber, )
supermod.ProductIDType141.subclass = ProductIDType141Sub
# end class ProductIDType141Sub


class NRFStandardColorAndSizeType142Sub(supermod.NRFStandardColorAndSizeType142):
    def __init__(self, NRFColorCode=None, ColorCategoryName=None, ColorPrimaryDescription=None, NRFSizeCode=None, SizeCategoryName=None, SizePrimaryDescription=None, SizeSecondaryDescription=None, SizeTableName=None, SizeHeading1=None, SizeHeading2=None, SizeHeading3=None, SizeHeading4=None):
        super(NRFStandardColorAndSizeType142Sub, self).__init__(NRFColorCode, ColorCategoryName, ColorPrimaryDescription, NRFSizeCode, SizeCategoryName, SizePrimaryDescription, SizeSecondaryDescription, SizeTableName, SizeHeading1, SizeHeading2, SizeHeading3, SizeHeading4, )
supermod.NRFStandardColorAndSizeType142.subclass = NRFStandardColorAndSizeType142Sub
# end class NRFStandardColorAndSizeType142Sub


class PhysicalDetailsType143Sub(supermod.PhysicalDetailsType143):
    def __init__(self, PackQualifier=None, PackValue=None, PackSize=None, PackUOM=None, PackingMedium=None, PackingMaterial=None, WeightQualifier=None, PackWeight=None, PackWeightUOM=None, PackVolume=None, PackVolumeUOM=None, PackLength=None, PackWidth=None, PackHeight=None, PackDimensionUOM=None, Description=None, SurfaceLayerPositionCode=None, AssignedID=None):
        super(PhysicalDetailsType143Sub, self).__init__(PackQualifier, PackValue, PackSize, PackUOM, PackingMedium, PackingMaterial, WeightQualifier, PackWeight, PackWeightUOM, PackVolume, PackVolumeUOM, PackLength, PackWidth, PackHeight, PackDimensionUOM, Description, SurfaceLayerPositionCode, AssignedID, )
supermod.PhysicalDetailsType143.subclass = PhysicalDetailsType143Sub
# end class PhysicalDetailsType143Sub


class CarrierSpecialHandlingDetailType144Sub(supermod.CarrierSpecialHandlingDetailType144):
    def __init__(self, SpecialHandlingCode=None, HazardousMaterialCode=None, HazardousMaterialClass=None, Description=None, YesOrNoResponse=None):
        super(CarrierSpecialHandlingDetailType144Sub, self).__init__(SpecialHandlingCode, HazardousMaterialCode, HazardousMaterialClass, Description, YesOrNoResponse, )
supermod.CarrierSpecialHandlingDetailType144.subclass = CarrierSpecialHandlingDetailType144Sub
# end class CarrierSpecialHandlingDetailType144Sub


class CarrierInformationType145Sub(supermod.CarrierInformationType145):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationType145Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType145.subclass = CarrierInformationType145Sub
# end class CarrierInformationType145Sub


class ServiceLevelCodesType146Sub(supermod.ServiceLevelCodesType146):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType146Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType146.subclass = ServiceLevelCodesType146Sub
# end class ServiceLevelCodesType146Sub


class AddressType147Sub(supermod.AddressType147):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType147Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType147.subclass = AddressType147Sub
# end class AddressType147Sub


class DateType148Sub(supermod.DateType148):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType148Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType148.subclass = DateType148Sub
# end class DateType148Sub


class MeasurementsType149Sub(supermod.MeasurementsType149):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType149Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType149.subclass = MeasurementsType149Sub
# end class MeasurementsType149Sub


class PriceInformationType150Sub(supermod.PriceInformationType150):
    def __init__(self, ChangeReasonCode=None, EffectiveDate=None, PriceTypeIDCode=None, UnitPrice=None, UnitPriceBasis=None, Currency=None, PriceMultiplierQual=None, PriceMultiplier=None, RebateAmount=None, Quantity=None, QuantityUOM=None, MultiplePriceQuantity=None, ClassOfTradeCode=None, ConditionValue=None, Description=None):
        super(PriceInformationType150Sub, self).__init__(ChangeReasonCode, EffectiveDate, PriceTypeIDCode, UnitPrice, UnitPriceBasis, Currency, PriceMultiplierQual, PriceMultiplier, RebateAmount, Quantity, QuantityUOM, MultiplePriceQuantity, ClassOfTradeCode, ConditionValue, Description, )
supermod.PriceInformationType150.subclass = PriceInformationType150Sub
# end class PriceInformationType150Sub


class ProductOrItemDescriptionType151Sub(supermod.ProductOrItemDescriptionType151):
    def __init__(self, ItemDescriptionType=None, ProductCharacteristicCode=None, AgencyQualifierCode=None, ProductDescriptionCode=None, ProductDescription=None, SurfaceLayerPositionCode=None, SourceSubqualifier=None, YesOrNoResponse=None, LanguageCode=None):
        super(ProductOrItemDescriptionType151Sub, self).__init__(ItemDescriptionType, ProductCharacteristicCode, AgencyQualifierCode, ProductDescriptionCode, ProductDescription, SurfaceLayerPositionCode, SourceSubqualifier, YesOrNoResponse, LanguageCode, )
supermod.ProductOrItemDescriptionType151.subclass = ProductOrItemDescriptionType151Sub
# end class ProductOrItemDescriptionType151Sub


class MasterItemAttributeType152Sub(supermod.MasterItemAttributeType152):
    def __init__(self, ItemAttribute=None):
        super(MasterItemAttributeType152Sub, self).__init__(ItemAttribute, )
supermod.MasterItemAttributeType152.subclass = MasterItemAttributeType152Sub
# end class MasterItemAttributeType152Sub


class ItemAttributeType153Sub(supermod.ItemAttributeType153):
    def __init__(self, ItemAttributeQualifier=None, Value=None, ValueUOM=None, Description=None, YesOrNoResponse=None, Measurements=None):
        super(ItemAttributeType153Sub, self).__init__(ItemAttributeQualifier, Value, ValueUOM, Description, YesOrNoResponse, Measurements, )
supermod.ItemAttributeType153.subclass = ItemAttributeType153Sub
# end class ItemAttributeType153Sub


class MeasurementsType154Sub(supermod.MeasurementsType154):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType154Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType154.subclass = MeasurementsType154Sub
# end class MeasurementsType154Sub


class DateType155Sub(supermod.DateType155):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType155Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType155.subclass = DateType155Sub
# end class DateType155Sub


class ReferenceType156Sub(supermod.ReferenceType156):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType156Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType156.subclass = ReferenceType156Sub
# end class ReferenceType156Sub


class ReferenceIDsType157Sub(supermod.ReferenceIDsType157):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType157Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType157.subclass = ReferenceIDsType157Sub
# end class ReferenceIDsType157Sub


class NotesType158Sub(supermod.NotesType158):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType158Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType158.subclass = NotesType158Sub
# end class NotesType158Sub


class CommodityType159Sub(supermod.CommodityType159):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType159Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType159.subclass = CommodityType159Sub
# end class CommodityType159Sub


class AddressType160Sub(supermod.AddressType160):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressType160Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType160.subclass = AddressType160Sub
# end class AddressType160Sub


class ReferenceType161Sub(supermod.ReferenceType161):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType161Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType161.subclass = ReferenceType161Sub
# end class ReferenceType161Sub


class ReferenceIDsType162Sub(supermod.ReferenceIDsType162):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType162Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType162.subclass = ReferenceIDsType162Sub
# end class ReferenceIDsType162Sub


class ContactType163Sub(supermod.ContactType163):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType163Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType163.subclass = ContactType163Sub
# end class ContactType163Sub


class AdditionalContactDetailsType164Sub(supermod.AdditionalContactDetailsType164):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType164Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType164.subclass = AdditionalContactDetailsType164Sub
# end class AdditionalContactDetailsType164Sub


class DateType165Sub(supermod.DateType165):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType165Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType165.subclass = DateType165Sub
# end class DateType165Sub


class SublinesType166Sub(supermod.SublinesType166):
    def __init__(self, Subline=None):
        super(SublinesType166Sub, self).__init__(Subline, )
supermod.SublinesType166.subclass = SublinesType166Sub
# end class SublinesType166Sub


class SublineType167Sub(supermod.SublineType167):
    def __init__(self, SublineItemDetail=None, PriceInformation=None, ProductOrItemDescription=None, Commodity=None):
        super(SublineType167Sub, self).__init__(SublineItemDetail, PriceInformation, ProductOrItemDescription, Commodity, )
supermod.SublineType167.subclass = SublineType167Sub
# end class SublineType167Sub


class SublineItemDetailType168Sub(supermod.SublineItemDetailType168):
    def __init__(self, LineSequenceNumber=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None, ProductSizeCode=None, ProductSizeDescription=None, ProductColorCode=None, ProductColorDescription=None, ProductMaterialCode=None, ProductMaterialDescription=None, ProductProcessCode=None, ProductProcessDescription=None, QtyPer=None, QtyPerUOM=None, PurchasePriceType=None, PurchasePrice=None, PurchasePriceBasis=None, NRFStandardColorAndSize=None):
        super(SublineItemDetailType168Sub, self).__init__(LineSequenceNumber, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, ProductSizeCode, ProductSizeDescription, ProductColorCode, ProductColorDescription, ProductMaterialCode, ProductMaterialDescription, ProductProcessCode, ProductProcessDescription, QtyPer, QtyPerUOM, PurchasePriceType, PurchasePrice, PurchasePriceBasis, NRFStandardColorAndSize, )
supermod.SublineItemDetailType168.subclass = SublineItemDetailType168Sub
# end class SublineItemDetailType168Sub


class ProductIDType169Sub(supermod.ProductIDType169):
    def __init__(self, PartNumberQual=None, PartNumber=None):
        super(ProductIDType169Sub, self).__init__(PartNumberQual, PartNumber, )
supermod.ProductIDType169.subclass = ProductIDType169Sub
# end class ProductIDType169Sub


class NRFStandardColorAndSizeType170Sub(supermod.NRFStandardColorAndSizeType170):
    def __init__(self, NRFColorCode=None, ColorCategoryName=None, ColorPrimaryDescription=None, NRFSizeCode=None, SizeCategoryName=None, SizePrimaryDescription=None, SizeSecondaryDescription=None, SizeTableName=None, SizeHeading1=None, SizeHeading2=None, SizeHeading3=None, SizeHeading4=None):
        super(NRFStandardColorAndSizeType170Sub, self).__init__(NRFColorCode, ColorCategoryName, ColorPrimaryDescription, NRFSizeCode, SizeCategoryName, SizePrimaryDescription, SizeSecondaryDescription, SizeTableName, SizeHeading1, SizeHeading2, SizeHeading3, SizeHeading4, )
supermod.NRFStandardColorAndSizeType170.subclass = NRFStandardColorAndSizeType170Sub
# end class NRFStandardColorAndSizeType170Sub


class PriceInformationType171Sub(supermod.PriceInformationType171):
    def __init__(self, ChangeReasonCode=None, EffectiveDate=None, PriceTypeIDCode=None, UnitPrice=None, UnitPriceBasis=None, Currency=None, PriceMultiplierQual=None, PriceMultiplier=None, RebateAmount=None, Quantity=None, QuantityUOM=None, MultiplePriceQuantity=None, ClassOfTradeCode=None, ConditionValue=None, Description=None):
        super(PriceInformationType171Sub, self).__init__(ChangeReasonCode, EffectiveDate, PriceTypeIDCode, UnitPrice, UnitPriceBasis, Currency, PriceMultiplierQual, PriceMultiplier, RebateAmount, Quantity, QuantityUOM, MultiplePriceQuantity, ClassOfTradeCode, ConditionValue, Description, )
supermod.PriceInformationType171.subclass = PriceInformationType171Sub
# end class PriceInformationType171Sub


class ProductOrItemDescriptionType172Sub(supermod.ProductOrItemDescriptionType172):
    def __init__(self, ItemDescriptionType=None, ProductCharacteristicCode=None, AgencyQualifierCode=None, ProductDescriptionCode=None, ProductDescription=None, SurfaceLayerPositionCode=None, SourceSubqualifier=None, YesOrNoResponse=None, LanguageCode=None):
        super(ProductOrItemDescriptionType172Sub, self).__init__(ItemDescriptionType, ProductCharacteristicCode, AgencyQualifierCode, ProductDescriptionCode, ProductDescription, SurfaceLayerPositionCode, SourceSubqualifier, YesOrNoResponse, LanguageCode, )
supermod.ProductOrItemDescriptionType172.subclass = ProductOrItemDescriptionType172Sub
# end class ProductOrItemDescriptionType172Sub


class CommodityType173Sub(supermod.CommodityType173):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType173Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType173.subclass = CommodityType173Sub
# end class CommodityType173Sub


class TaxType174Sub(supermod.TaxType174):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType174Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType174.subclass = TaxType174Sub
# end class TaxType174Sub


class ChargesAllowancesType175Sub(supermod.ChargesAllowancesType175):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, Tax=None):
        super(ChargesAllowancesType175Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, Tax, )
supermod.ChargesAllowancesType175.subclass = ChargesAllowancesType175Sub
# end class ChargesAllowancesType175Sub


class TaxType176Sub(supermod.TaxType176):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType176Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType176.subclass = TaxType176Sub
# end class TaxType176Sub


class ItemLoadInfoType177Sub(supermod.ItemLoadInfoType177):
    def __init__(self, ItemLoad=None, Reference=None, Notes=None):
        super(ItemLoadInfoType177Sub, self).__init__(ItemLoad, Reference, Notes, )
supermod.ItemLoadInfoType177.subclass = ItemLoadInfoType177Sub
# end class ItemLoadInfoType177Sub


class ItemLoadType178Sub(supermod.ItemLoadType178):
    def __init__(self, NumberOfLoads=None, UnitsShipped=None, PackingMedium=None, PackingMaterial=None, LoadSize=None, LoadSizeUOM=None):
        super(ItemLoadType178Sub, self).__init__(NumberOfLoads, UnitsShipped, PackingMedium, PackingMaterial, LoadSize, LoadSizeUOM, )
supermod.ItemLoadType178.subclass = ItemLoadType178Sub
# end class ItemLoadType178Sub


class ReferenceType179Sub(supermod.ReferenceType179):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType179Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType179.subclass = ReferenceType179Sub
# end class ReferenceType179Sub


class ReferenceIDsType180Sub(supermod.ReferenceIDsType180):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType180Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType180.subclass = ReferenceIDsType180Sub
# end class ReferenceIDsType180Sub


class NotesType181Sub(supermod.NotesType181):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType181Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType181.subclass = NotesType181Sub
# end class NotesType181Sub


class SummaryTypeSub(supermod.SummaryType):
    def __init__(self, TotalOrders=None, TotalLineItems=None, TotalQuantity=None, TotalWeight=None):
        super(SummaryTypeSub, self).__init__(TotalOrders, TotalLineItems, TotalQuantity, TotalWeight, )
supermod.SummaryType.subclass = SummaryTypeSub
# end class SummaryTypeSub


class ContainerTypeSub(supermod.ContainerType):
    def __init__(self, BillOfLadingNumber=None, CarrierProNumber=None):
        super(ContainerTypeSub, self).__init__(BillOfLadingNumber, CarrierProNumber, )
supermod.ContainerType.subclass = ContainerTypeSub
# end class ContainerTypeSub


class DateType182Sub(supermod.DateType182):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType182Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType182.subclass = DateType182Sub
# end class DateType182Sub


class ReferenceType183Sub(supermod.ReferenceType183):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType183Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType183.subclass = ReferenceType183Sub
# end class ReferenceType183Sub


class ReferenceIDsType184Sub(supermod.ReferenceIDsType184):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType184Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType184.subclass = ReferenceIDsType184Sub
# end class ReferenceIDsType184Sub


class NotesType185Sub(supermod.NotesType185):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType185Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType185.subclass = NotesType185Sub
# end class NotesType185Sub


class QuantityAndWeightType186Sub(supermod.QuantityAndWeightType186):
    def __init__(self, PackingMedium=None, PackingMaterial=None, LadingQuantity=None, LadingDescription=None, WeightQualifier=None, Weight=None, WeightUOM=None, Volume=None, VolumeUOM=None, PalletExchangeCode=None):
        super(QuantityAndWeightType186Sub, self).__init__(PackingMedium, PackingMaterial, LadingQuantity, LadingDescription, WeightQualifier, Weight, WeightUOM, Volume, VolumeUOM, PalletExchangeCode, )
supermod.QuantityAndWeightType186.subclass = QuantityAndWeightType186Sub
# end class QuantityAndWeightType186Sub


class CarrierInformationType187Sub(supermod.CarrierInformationType187):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationType187Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType187.subclass = CarrierInformationType187Sub
# end class CarrierInformationType187Sub


class ServiceLevelCodesType188Sub(supermod.ServiceLevelCodesType188):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType188Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType188.subclass = ServiceLevelCodesType188Sub
# end class ServiceLevelCodesType188Sub


class AddressType189Sub(supermod.AddressType189):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType189Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType189.subclass = AddressType189Sub
# end class AddressType189Sub


class DateType190Sub(supermod.DateType190):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType190Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType190.subclass = DateType190Sub
# end class DateType190Sub


class AddressType191Sub(supermod.AddressType191):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressType191Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType191.subclass = AddressType191Sub
# end class AddressType191Sub


class ReferenceType192Sub(supermod.ReferenceType192):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType192Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType192.subclass = ReferenceType192Sub
# end class ReferenceType192Sub


class ReferenceIDsType193Sub(supermod.ReferenceIDsType193):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType193Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType193.subclass = ReferenceIDsType193Sub
# end class ReferenceIDsType193Sub


class ContactType194Sub(supermod.ContactType194):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType194Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType194.subclass = ContactType194Sub
# end class ContactType194Sub


class AdditionalContactDetailsType195Sub(supermod.AdditionalContactDetailsType195):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType195Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType195.subclass = AdditionalContactDetailsType195Sub
# end class AdditionalContactDetailsType195Sub


class DateType196Sub(supermod.DateType196):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType196Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType196.subclass = DateType196Sub
# end class DateType196Sub


class OrderHeaderType197Sub(supermod.OrderHeaderType197):
    def __init__(self, InternalOrderNumber=None, InternalOrderDate=None, InvoiceNumber=None, InvoiceDate=None, PurchaseOrderNumber=None, ReleaseNumber=None, PurchaseOrderDate=None, Department=None, DepartmentDescription=None, Vendor=None, JobNumber=None, Division=None, CustomerAccountNumber=None, CustomerOrderNumber=None, PromotionDealNumber=None, PromotionDealDescription=None, DeliveryDate=None, DeliveryTime=None):
        super(OrderHeaderType197Sub, self).__init__(InternalOrderNumber, InternalOrderDate, InvoiceNumber, InvoiceDate, PurchaseOrderNumber, ReleaseNumber, PurchaseOrderDate, Department, DepartmentDescription, Vendor, JobNumber, Division, CustomerAccountNumber, CustomerOrderNumber, PromotionDealNumber, PromotionDealDescription, DeliveryDate, DeliveryTime, )
supermod.OrderHeaderType197.subclass = OrderHeaderType197Sub
# end class OrderHeaderType197Sub


class QuantityAndWeightType198Sub(supermod.QuantityAndWeightType198):
    def __init__(self, PackingMedium=None, PackingMaterial=None, LadingQuantity=None, LadingDescription=None, WeightQualifier=None, Weight=None, WeightUOM=None, Volume=None, VolumeUOM=None, PalletExchangeCode=None):
        super(QuantityAndWeightType198Sub, self).__init__(PackingMedium, PackingMaterial, LadingQuantity, LadingDescription, WeightQualifier, Weight, WeightUOM, Volume, VolumeUOM, PalletExchangeCode, )
supermod.QuantityAndWeightType198.subclass = QuantityAndWeightType198Sub
# end class QuantityAndWeightType198Sub


class CarrierInformationType199Sub(supermod.CarrierInformationType199):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationType199Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType199.subclass = CarrierInformationType199Sub
# end class CarrierInformationType199Sub


class ServiceLevelCodesType200Sub(supermod.ServiceLevelCodesType200):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType200Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType200.subclass = ServiceLevelCodesType200Sub
# end class ServiceLevelCodesType200Sub


class AddressType201Sub(supermod.AddressType201):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType201Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType201.subclass = AddressType201Sub
# end class AddressType201Sub


class DateType202Sub(supermod.DateType202):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType202Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType202.subclass = DateType202Sub
# end class DateType202Sub


class DateType203Sub(supermod.DateType203):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType203Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType203.subclass = DateType203Sub
# end class DateType203Sub


class ReferenceType204Sub(supermod.ReferenceType204):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType204Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType204.subclass = ReferenceType204Sub
# end class ReferenceType204Sub


class ReferenceIDsType205Sub(supermod.ReferenceIDsType205):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType205Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType205.subclass = ReferenceIDsType205Sub
# end class ReferenceIDsType205Sub


class NotesType206Sub(supermod.NotesType206):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType206Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType206.subclass = NotesType206Sub
# end class NotesType206Sub


class AddressType207Sub(supermod.AddressType207):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressType207Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType207.subclass = AddressType207Sub
# end class AddressType207Sub


class ReferenceType208Sub(supermod.ReferenceType208):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType208Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType208.subclass = ReferenceType208Sub
# end class ReferenceType208Sub


class ReferenceIDsType209Sub(supermod.ReferenceIDsType209):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType209Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType209.subclass = ReferenceIDsType209Sub
# end class ReferenceIDsType209Sub


class ContactType210Sub(supermod.ContactType210):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType210Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType210.subclass = ContactType210Sub
# end class ContactType210Sub


class AdditionalContactDetailsType211Sub(supermod.AdditionalContactDetailsType211):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType211Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType211.subclass = AdditionalContactDetailsType211Sub
# end class AdditionalContactDetailsType211Sub


class DateType212Sub(supermod.DateType212):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType212Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType212.subclass = DateType212Sub
# end class DateType212Sub


class TaxType213Sub(supermod.TaxType213):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType213Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType213.subclass = TaxType213Sub
# end class TaxType213Sub


class ChargesAllowancesType214Sub(supermod.ChargesAllowancesType214):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, Tax=None):
        super(ChargesAllowancesType214Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, Tax, )
supermod.ChargesAllowancesType214.subclass = ChargesAllowancesType214Sub
# end class ChargesAllowancesType214Sub


class TaxType215Sub(supermod.TaxType215):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType215Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType215.subclass = TaxType215Sub
# end class TaxType215Sub


class CommodityType216Sub(supermod.CommodityType216):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType216Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType216.subclass = CommodityType216Sub
# end class CommodityType216Sub


class PackType217Sub(supermod.PackType217):
    def __init__(self, PackLevelType=None, ShippingSerialID=None, CarrierPackageID=None):
        super(PackType217Sub, self).__init__(PackLevelType, ShippingSerialID, CarrierPackageID, )
supermod.PackType217.subclass = PackType217Sub
# end class PackType217Sub


class PhysicalDetailsType218Sub(supermod.PhysicalDetailsType218):
    def __init__(self, PackQualifier=None, PackValue=None, PackSize=None, PackUOM=None, PackingMedium=None, PackingMaterial=None, WeightQualifier=None, PackWeight=None, PackWeightUOM=None, PackVolume=None, PackVolumeUOM=None, PackLength=None, PackWidth=None, PackHeight=None, PackDimensionUOM=None, Description=None, SurfaceLayerPositionCode=None, AssignedID=None):
        super(PhysicalDetailsType218Sub, self).__init__(PackQualifier, PackValue, PackSize, PackUOM, PackingMedium, PackingMaterial, WeightQualifier, PackWeight, PackWeightUOM, PackVolume, PackVolumeUOM, PackLength, PackWidth, PackHeight, PackDimensionUOM, Description, SurfaceLayerPositionCode, AssignedID, )
supermod.PhysicalDetailsType218.subclass = PhysicalDetailsType218Sub
# end class PhysicalDetailsType218Sub


class MarksAndNumbersCollectionType219Sub(supermod.MarksAndNumbersCollectionType219):
    def __init__(self, MarksAndNumbersQualifier1=None, MarksAndNumbers1=None):
        super(MarksAndNumbersCollectionType219Sub, self).__init__(MarksAndNumbersQualifier1, MarksAndNumbers1, )
supermod.MarksAndNumbersCollectionType219.subclass = MarksAndNumbersCollectionType219Sub
# end class MarksAndNumbersCollectionType219Sub


class PalletInformationType220Sub(supermod.PalletInformationType220):
    def __init__(self, PalletQualifier=None, PalletValue=None, PalletTypeCode=None, PalletTiers=None, PalletBlocks=None, UnitWeight=None, UnitWeightUOM=None, Length=None, Width=None, Height=None, UnitOfMeasure=None, WeightQualifier=None, PalletWeight=None, PalletWeightUOM=None, PalletVolume=None, PalletVolumeUOM=None, PalletExchangeCode=None, PalletStructureCode=None):
        super(PalletInformationType220Sub, self).__init__(PalletQualifier, PalletValue, PalletTypeCode, PalletTiers, PalletBlocks, UnitWeight, UnitWeightUOM, Length, Width, Height, UnitOfMeasure, WeightQualifier, PalletWeight, PalletWeightUOM, PalletVolume, PalletVolumeUOM, PalletExchangeCode, PalletStructureCode, )
supermod.PalletInformationType220.subclass = PalletInformationType220Sub
# end class PalletInformationType220Sub


class DateType221Sub(supermod.DateType221):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType221Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType221.subclass = DateType221Sub
# end class DateType221Sub


class ReferenceType222Sub(supermod.ReferenceType222):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType222Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType222.subclass = ReferenceType222Sub
# end class ReferenceType222Sub


class ReferenceIDsType223Sub(supermod.ReferenceIDsType223):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType223Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType223.subclass = ReferenceIDsType223Sub
# end class ReferenceIDsType223Sub


class NotesType224Sub(supermod.NotesType224):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType224Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType224.subclass = NotesType224Sub
# end class NotesType224Sub


class AddressType225Sub(supermod.AddressType225):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressType225Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType225.subclass = AddressType225Sub
# end class AddressType225Sub


class ReferenceType226Sub(supermod.ReferenceType226):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType226Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType226.subclass = ReferenceType226Sub
# end class ReferenceType226Sub


class ReferenceIDsType227Sub(supermod.ReferenceIDsType227):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType227Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType227.subclass = ReferenceIDsType227Sub
# end class ReferenceIDsType227Sub


class ContactType228Sub(supermod.ContactType228):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType228Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType228.subclass = ContactType228Sub
# end class ContactType228Sub


class AdditionalContactDetailsType229Sub(supermod.AdditionalContactDetailsType229):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType229Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType229.subclass = AdditionalContactDetailsType229Sub
# end class AdditionalContactDetailsType229Sub


class DateType230Sub(supermod.DateType230):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType230Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType230.subclass = DateType230Sub
# end class DateType230Sub


class TaxType231Sub(supermod.TaxType231):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType231Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType231.subclass = TaxType231Sub
# end class TaxType231Sub


class ChargesAllowancesType232Sub(supermod.ChargesAllowancesType232):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, Tax=None):
        super(ChargesAllowancesType232Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, Tax, )
supermod.ChargesAllowancesType232.subclass = ChargesAllowancesType232Sub
# end class ChargesAllowancesType232Sub


class TaxType233Sub(supermod.TaxType233):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType233Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType233.subclass = TaxType233Sub
# end class TaxType233Sub


class CarrierInformationType234Sub(supermod.CarrierInformationType234):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationType234Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType234.subclass = CarrierInformationType234Sub
# end class CarrierInformationType234Sub


class ServiceLevelCodesType235Sub(supermod.ServiceLevelCodesType235):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType235Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType235.subclass = ServiceLevelCodesType235Sub
# end class ServiceLevelCodesType235Sub


class AddressType236Sub(supermod.AddressType236):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType236Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType236.subclass = AddressType236Sub
# end class AddressType236Sub


class DateType237Sub(supermod.DateType237):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType237Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType237.subclass = DateType237Sub
# end class DateType237Sub


class PackagingType238Sub(supermod.PackagingType238):
    def __init__(self, ItemDescriptionType=None, PackagingCharacteristicCode=None, AgencyQualifierCode=None, PackagingDescriptionCode=None, PackagingDescription=None, UnitLoadOptionCode=None):
        super(PackagingType238Sub, self).__init__(ItemDescriptionType, PackagingCharacteristicCode, AgencyQualifierCode, PackagingDescriptionCode, PackagingDescription, UnitLoadOptionCode, )
supermod.PackagingType238.subclass = PackagingType238Sub
# end class PackagingType238Sub


class ShipmentLineType239Sub(supermod.ShipmentLineType239):
    def __init__(self, LineSequenceNumber=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None, OrderQty=None, OrderQtyUOM=None, PurchasePriceType=None, PurchasePrice=None, PurchasePriceBasis=None, ItemStatusCode=None, ShipQty=None, ShipQtyUOM=None, ShipDate=None, QtyLeftToReceive=None, ProductSizeCode=None, ProductSizeDescription=None, ProductColorCode=None, ProductColorDescription=None, ProductMaterialCode=None, ProductMaterialDescription=None, ProductProcessCode=None, ProductProcessDescription=None, Department=None, DepartmentDescription=None, Class=None, SellerDateCode=None, NRFStandardColorAndSize=None):
        super(ShipmentLineType239Sub, self).__init__(LineSequenceNumber, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, OrderQty, OrderQtyUOM, PurchasePriceType, PurchasePrice, PurchasePriceBasis, ItemStatusCode, ShipQty, ShipQtyUOM, ShipDate, QtyLeftToReceive, ProductSizeCode, ProductSizeDescription, ProductColorCode, ProductColorDescription, ProductMaterialCode, ProductMaterialDescription, ProductProcessCode, ProductProcessDescription, Department, DepartmentDescription, Class, SellerDateCode, NRFStandardColorAndSize, )
supermod.ShipmentLineType239.subclass = ShipmentLineType239Sub
# end class ShipmentLineType239Sub


class ProductIDType240Sub(supermod.ProductIDType240):
    def __init__(self, PartNumberQual=None, PartNumber=None):
        super(ProductIDType240Sub, self).__init__(PartNumberQual, PartNumber, )
supermod.ProductIDType240.subclass = ProductIDType240Sub
# end class ProductIDType240Sub


class NRFStandardColorAndSizeType241Sub(supermod.NRFStandardColorAndSizeType241):
    def __init__(self, NRFColorCode=None, ColorCategoryName=None, ColorPrimaryDescription=None, NRFSizeCode=None, SizeCategoryName=None, SizePrimaryDescription=None, SizeSecondaryDescription=None, SizeTableName=None, SizeHeading1=None, SizeHeading2=None, SizeHeading3=None, SizeHeading4=None):
        super(NRFStandardColorAndSizeType241Sub, self).__init__(NRFColorCode, ColorCategoryName, ColorPrimaryDescription, NRFSizeCode, SizeCategoryName, SizePrimaryDescription, SizeSecondaryDescription, SizeTableName, SizeHeading1, SizeHeading2, SizeHeading3, SizeHeading4, )
supermod.NRFStandardColorAndSizeType241.subclass = NRFStandardColorAndSizeType241Sub
# end class NRFStandardColorAndSizeType241Sub


class PhysicalDetailsType242Sub(supermod.PhysicalDetailsType242):
    def __init__(self, PackQualifier=None, PackValue=None, PackSize=None, PackUOM=None, PackingMedium=None, PackingMaterial=None, WeightQualifier=None, PackWeight=None, PackWeightUOM=None, PackVolume=None, PackVolumeUOM=None, PackLength=None, PackWidth=None, PackHeight=None, PackDimensionUOM=None, Description=None, SurfaceLayerPositionCode=None, AssignedID=None):
        super(PhysicalDetailsType242Sub, self).__init__(PackQualifier, PackValue, PackSize, PackUOM, PackingMedium, PackingMaterial, WeightQualifier, PackWeight, PackWeightUOM, PackVolume, PackVolumeUOM, PackLength, PackWidth, PackHeight, PackDimensionUOM, Description, SurfaceLayerPositionCode, AssignedID, )
supermod.PhysicalDetailsType242.subclass = PhysicalDetailsType242Sub
# end class PhysicalDetailsType242Sub


class CarrierSpecialHandlingDetailType243Sub(supermod.CarrierSpecialHandlingDetailType243):
    def __init__(self, SpecialHandlingCode=None, HazardousMaterialCode=None, HazardousMaterialClass=None, Description=None, YesOrNoResponse=None):
        super(CarrierSpecialHandlingDetailType243Sub, self).__init__(SpecialHandlingCode, HazardousMaterialCode, HazardousMaterialClass, Description, YesOrNoResponse, )
supermod.CarrierSpecialHandlingDetailType243.subclass = CarrierSpecialHandlingDetailType243Sub
# end class CarrierSpecialHandlingDetailType243Sub


class CarrierInformationType244Sub(supermod.CarrierInformationType244):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, SealStatusCode=None, SealNumber=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None):
        super(CarrierInformationType244Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, SealStatusCode, SealNumber, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, )
supermod.CarrierInformationType244.subclass = CarrierInformationType244Sub
# end class CarrierInformationType244Sub


class ServiceLevelCodesType245Sub(supermod.ServiceLevelCodesType245):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType245Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType245.subclass = ServiceLevelCodesType245Sub
# end class ServiceLevelCodesType245Sub


class AddressType246Sub(supermod.AddressType246):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Date=None):
        super(AddressType246Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Date, )
supermod.AddressType246.subclass = AddressType246Sub
# end class AddressType246Sub


class DateType247Sub(supermod.DateType247):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType247Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType247.subclass = DateType247Sub
# end class DateType247Sub


class MeasurementsType248Sub(supermod.MeasurementsType248):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType248Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType248.subclass = MeasurementsType248Sub
# end class MeasurementsType248Sub


class PriceInformationType249Sub(supermod.PriceInformationType249):
    def __init__(self, ChangeReasonCode=None, EffectiveDate=None, PriceTypeIDCode=None, UnitPrice=None, UnitPriceBasis=None, Currency=None, PriceMultiplierQual=None, PriceMultiplier=None, RebateAmount=None, Quantity=None, QuantityUOM=None, MultiplePriceQuantity=None, ClassOfTradeCode=None, ConditionValue=None, Description=None):
        super(PriceInformationType249Sub, self).__init__(ChangeReasonCode, EffectiveDate, PriceTypeIDCode, UnitPrice, UnitPriceBasis, Currency, PriceMultiplierQual, PriceMultiplier, RebateAmount, Quantity, QuantityUOM, MultiplePriceQuantity, ClassOfTradeCode, ConditionValue, Description, )
supermod.PriceInformationType249.subclass = PriceInformationType249Sub
# end class PriceInformationType249Sub


class ProductOrItemDescriptionType250Sub(supermod.ProductOrItemDescriptionType250):
    def __init__(self, ItemDescriptionType=None, ProductCharacteristicCode=None, AgencyQualifierCode=None, ProductDescriptionCode=None, ProductDescription=None, SurfaceLayerPositionCode=None, SourceSubqualifier=None, YesOrNoResponse=None, LanguageCode=None):
        super(ProductOrItemDescriptionType250Sub, self).__init__(ItemDescriptionType, ProductCharacteristicCode, AgencyQualifierCode, ProductDescriptionCode, ProductDescription, SurfaceLayerPositionCode, SourceSubqualifier, YesOrNoResponse, LanguageCode, )
supermod.ProductOrItemDescriptionType250.subclass = ProductOrItemDescriptionType250Sub
# end class ProductOrItemDescriptionType250Sub


class MasterItemAttributeType251Sub(supermod.MasterItemAttributeType251):
    def __init__(self, ItemAttribute=None):
        super(MasterItemAttributeType251Sub, self).__init__(ItemAttribute, )
supermod.MasterItemAttributeType251.subclass = MasterItemAttributeType251Sub
# end class MasterItemAttributeType251Sub


class ItemAttributeType252Sub(supermod.ItemAttributeType252):
    def __init__(self, ItemAttributeQualifier=None, Value=None, ValueUOM=None, Description=None, YesOrNoResponse=None, Measurements=None):
        super(ItemAttributeType252Sub, self).__init__(ItemAttributeQualifier, Value, ValueUOM, Description, YesOrNoResponse, Measurements, )
supermod.ItemAttributeType252.subclass = ItemAttributeType252Sub
# end class ItemAttributeType252Sub


class MeasurementsType253Sub(supermod.MeasurementsType253):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType253Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType253.subclass = MeasurementsType253Sub
# end class MeasurementsType253Sub


class DateType254Sub(supermod.DateType254):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType254Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType254.subclass = DateType254Sub
# end class DateType254Sub


class ReferenceType255Sub(supermod.ReferenceType255):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType255Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType255.subclass = ReferenceType255Sub
# end class ReferenceType255Sub


class ReferenceIDsType256Sub(supermod.ReferenceIDsType256):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType256Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType256.subclass = ReferenceIDsType256Sub
# end class ReferenceIDsType256Sub


class NotesType257Sub(supermod.NotesType257):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType257Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType257.subclass = NotesType257Sub
# end class NotesType257Sub


class CommodityType258Sub(supermod.CommodityType258):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType258Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType258.subclass = CommodityType258Sub
# end class CommodityType258Sub


class AddressType259Sub(supermod.AddressType259):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Reference=None, Contact=None, Date=None):
        super(AddressType259Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Reference, Contact, Date, )
supermod.AddressType259.subclass = AddressType259Sub
# end class AddressType259Sub


class ReferenceType260Sub(supermod.ReferenceType260):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType260Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType260.subclass = ReferenceType260Sub
# end class ReferenceType260Sub


class ReferenceIDsType261Sub(supermod.ReferenceIDsType261):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType261Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType261.subclass = ReferenceIDsType261Sub
# end class ReferenceIDsType261Sub


class ContactType262Sub(supermod.ContactType262):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactType262Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactType262.subclass = ContactType262Sub
# end class ContactType262Sub


class AdditionalContactDetailsType263Sub(supermod.AdditionalContactDetailsType263):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType263Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType263.subclass = AdditionalContactDetailsType263Sub
# end class AdditionalContactDetailsType263Sub


class DateType264Sub(supermod.DateType264):
    def __init__(self, DateTimeQualifier1=None, Date1=None, Time1=None, DateTimePeriod=None):
        super(DateType264Sub, self).__init__(DateTimeQualifier1, Date1, Time1, DateTimePeriod, )
supermod.DateType264.subclass = DateType264Sub
# end class DateType264Sub


class SublinesType265Sub(supermod.SublinesType265):
    def __init__(self, Subline=None):
        super(SublinesType265Sub, self).__init__(Subline, )
supermod.SublinesType265.subclass = SublinesType265Sub
# end class SublinesType265Sub


class SublineType266Sub(supermod.SublineType266):
    def __init__(self, SublineItemDetail=None, PriceInformation=None, ProductOrItemDescription=None, Commodity=None):
        super(SublineType266Sub, self).__init__(SublineItemDetail, PriceInformation, ProductOrItemDescription, Commodity, )
supermod.SublineType266.subclass = SublineType266Sub
# end class SublineType266Sub


class SublineItemDetailType267Sub(supermod.SublineItemDetailType267):
    def __init__(self, LineSequenceNumber=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None, ProductSizeCode=None, ProductSizeDescription=None, ProductColorCode=None, ProductColorDescription=None, ProductMaterialCode=None, ProductMaterialDescription=None, ProductProcessCode=None, ProductProcessDescription=None, QtyPer=None, QtyPerUOM=None, PurchasePriceType=None, PurchasePrice=None, PurchasePriceBasis=None, NRFStandardColorAndSize=None):
        super(SublineItemDetailType267Sub, self).__init__(LineSequenceNumber, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, ProductSizeCode, ProductSizeDescription, ProductColorCode, ProductColorDescription, ProductMaterialCode, ProductMaterialDescription, ProductProcessCode, ProductProcessDescription, QtyPer, QtyPerUOM, PurchasePriceType, PurchasePrice, PurchasePriceBasis, NRFStandardColorAndSize, )
supermod.SublineItemDetailType267.subclass = SublineItemDetailType267Sub
# end class SublineItemDetailType267Sub


class ProductIDType268Sub(supermod.ProductIDType268):
    def __init__(self, PartNumberQual=None, PartNumber=None):
        super(ProductIDType268Sub, self).__init__(PartNumberQual, PartNumber, )
supermod.ProductIDType268.subclass = ProductIDType268Sub
# end class ProductIDType268Sub


class NRFStandardColorAndSizeType269Sub(supermod.NRFStandardColorAndSizeType269):
    def __init__(self, NRFColorCode=None, ColorCategoryName=None, ColorPrimaryDescription=None, NRFSizeCode=None, SizeCategoryName=None, SizePrimaryDescription=None, SizeSecondaryDescription=None, SizeTableName=None, SizeHeading1=None, SizeHeading2=None, SizeHeading3=None, SizeHeading4=None):
        super(NRFStandardColorAndSizeType269Sub, self).__init__(NRFColorCode, ColorCategoryName, ColorPrimaryDescription, NRFSizeCode, SizeCategoryName, SizePrimaryDescription, SizeSecondaryDescription, SizeTableName, SizeHeading1, SizeHeading2, SizeHeading3, SizeHeading4, )
supermod.NRFStandardColorAndSizeType269.subclass = NRFStandardColorAndSizeType269Sub
# end class NRFStandardColorAndSizeType269Sub


class PriceInformationType270Sub(supermod.PriceInformationType270):
    def __init__(self, ChangeReasonCode=None, EffectiveDate=None, PriceTypeIDCode=None, UnitPrice=None, UnitPriceBasis=None, Currency=None, PriceMultiplierQual=None, PriceMultiplier=None, RebateAmount=None, Quantity=None, QuantityUOM=None, MultiplePriceQuantity=None, ClassOfTradeCode=None, ConditionValue=None, Description=None):
        super(PriceInformationType270Sub, self).__init__(ChangeReasonCode, EffectiveDate, PriceTypeIDCode, UnitPrice, UnitPriceBasis, Currency, PriceMultiplierQual, PriceMultiplier, RebateAmount, Quantity, QuantityUOM, MultiplePriceQuantity, ClassOfTradeCode, ConditionValue, Description, )
supermod.PriceInformationType270.subclass = PriceInformationType270Sub
# end class PriceInformationType270Sub


class ProductOrItemDescriptionType271Sub(supermod.ProductOrItemDescriptionType271):
    def __init__(self, ItemDescriptionType=None, ProductCharacteristicCode=None, AgencyQualifierCode=None, ProductDescriptionCode=None, ProductDescription=None, SurfaceLayerPositionCode=None, SourceSubqualifier=None, YesOrNoResponse=None, LanguageCode=None):
        super(ProductOrItemDescriptionType271Sub, self).__init__(ItemDescriptionType, ProductCharacteristicCode, AgencyQualifierCode, ProductDescriptionCode, ProductDescription, SurfaceLayerPositionCode, SourceSubqualifier, YesOrNoResponse, LanguageCode, )
supermod.ProductOrItemDescriptionType271.subclass = ProductOrItemDescriptionType271Sub
# end class ProductOrItemDescriptionType271Sub


class CommodityType272Sub(supermod.CommodityType272):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType272Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType272.subclass = CommodityType272Sub
# end class CommodityType272Sub


class TaxType273Sub(supermod.TaxType273):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType273Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType273.subclass = TaxType273Sub
# end class TaxType273Sub


class ChargesAllowancesType274Sub(supermod.ChargesAllowancesType274):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, Tax=None):
        super(ChargesAllowancesType274Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, Tax, )
supermod.ChargesAllowancesType274.subclass = ChargesAllowancesType274Sub
# end class ChargesAllowancesType274Sub


class TaxType275Sub(supermod.TaxType275):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PctDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxType275Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PctDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxType275.subclass = TaxType275Sub
# end class TaxType275Sub


class ItemLoadInfoType276Sub(supermod.ItemLoadInfoType276):
    def __init__(self, ItemLoad=None, Reference=None, Notes=None):
        super(ItemLoadInfoType276Sub, self).__init__(ItemLoad, Reference, Notes, )
supermod.ItemLoadInfoType276.subclass = ItemLoadInfoType276Sub
# end class ItemLoadInfoType276Sub


class ItemLoadType277Sub(supermod.ItemLoadType277):
    def __init__(self, NumberOfLoads=None, UnitsShipped=None, PackingMedium=None, PackingMaterial=None, LoadSize=None, LoadSizeUOM=None):
        super(ItemLoadType277Sub, self).__init__(NumberOfLoads, UnitsShipped, PackingMedium, PackingMaterial, LoadSize, LoadSizeUOM, )
supermod.ItemLoadType277.subclass = ItemLoadType277Sub
# end class ItemLoadType277Sub


class ReferenceType278Sub(supermod.ReferenceType278):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date1=None, Time1=None, ReferenceIDs=None):
        super(ReferenceType278Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date1, Time1, ReferenceIDs, )
supermod.ReferenceType278.subclass = ReferenceType278Sub
# end class ReferenceType278Sub


class ReferenceIDsType279Sub(supermod.ReferenceIDsType279):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType279Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType279.subclass = ReferenceIDsType279Sub
# end class ReferenceIDsType279Sub


class NotesType280Sub(supermod.NotesType280):
    def __init__(self, NoteCode=None, NoteInformationField=None, LanguageCode=None, NoteFormatCode=None, NoteFunctionCode=None):
        super(NotesType280Sub, self).__init__(NoteCode, NoteInformationField, LanguageCode, NoteFormatCode, NoteFunctionCode, )
supermod.NotesType280.subclass = NotesType280Sub
# end class NotesType280Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Shipments'
        rootClass = supermod.Shipments
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Shipments'
        rootClass = supermod.Shipments
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Shipments'
        rootClass = supermod.Shipments
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Shipments'
        rootClass = supermod.Shipments
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from Shipments import *\n\n')
        sys.stdout.write('import Shipments as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
