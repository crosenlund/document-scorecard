#!/usr/bin/env python

#
# Generated Tue Jan 10 20:16:33 2017 by generateDS.py version 2.22a.
#
# Command line options:
#   ('-f', '')
#   ('-o', 'app/SCHEMA_LAYOUTS/Order-e.py')
#   ('-s', 'Order.py')
#   ('--super', 'Orders')
#
# Command line arguments:
#   app/SCHEMAS/Order-e.xsd
#
# Command line:
#   generateDS/generateDS.py -f -o "app/SCHEMA_LAYOUTS/Order-e.py" -s "Order.py" --super="Orders" app/SCHEMAS/Order-e.xsd
#
# Current working directory (os.getcwd()):
#   document-scorecard-v2
#

import sys
from lxml import etree as etree_

import Orders as supermod

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


class OrdersSub(supermod.Orders):
    def __init__(self, Order=None):
        super(OrdersSub, self).__init__(Order, )
supermod.Orders.subclass = OrdersSub
# end class OrdersSub


class OrderTypeSub(supermod.OrderType):
    def __init__(self, Meta=None, Header=None, LineItem=None, Summary=None):
        super(OrderTypeSub, self).__init__(Meta, Header, LineItem, Summary, )
supermod.OrderType.subclass = OrderTypeSub
# end class OrderTypeSub


class attributes_stringSub(supermod.attributes_string):
    def __init__(self, requires_one=None, requires_others=None, not_equal=None, score=None, qualified_rep=None, valueOf_=None):
        super(attributes_stringSub, self).__init__(requires_one, requires_others, not_equal, score, qualified_rep, valueOf_, )
supermod.attributes_string.subclass = attributes_stringSub
# end class attributes_stringSub


class MetaTypeSub(supermod.MetaType):
    def __init__(self, SenderUniqueID=None, SenderCompanyName=None, ReceiverUniqueID=None, ReceiverCompanyName=None, IsDropShip=None, InterchangeControlNumber=None, GroupControlIdentifier=None, GroupControlNumber=None, DocumentControlIdentifier=None, DocumentControlNumber=None, InterchangeSenderID=None, InterchangeReceiverID=None, GroupSenderID=None, GroupReceiverID=None, BatchPart=None, BatchTotal=None, BatchID=None, Comments=None, Validation=None, OrderManagement=None, Version=None):
        super(MetaTypeSub, self).__init__(SenderUniqueID, SenderCompanyName, ReceiverUniqueID, ReceiverCompanyName, IsDropShip, InterchangeControlNumber, GroupControlIdentifier, GroupControlNumber, DocumentControlIdentifier, DocumentControlNumber, InterchangeSenderID, InterchangeReceiverID, GroupSenderID, GroupReceiverID, BatchPart, BatchTotal, BatchID, Comments, Validation, OrderManagement, Version, )
supermod.MetaType.subclass = MetaTypeSub
# end class MetaTypeSub


class HeaderTypeSub(supermod.HeaderType):
    def __init__(self, OrderHeader=None, PaymentTerms=None, Dates=None, Contacts=None, Address=None, FOBRelatedInstruction=None, Commodity=None, Measurements=None, Paperwork=None, Packaging=None, QuantityAndWeight=None, CarrierInformation=None, CarrierSpecialHandlingDetail=None, MarksAndNumbersCollection=None, RestrictionsOrConditions=None, LeadTime=None, References=None, Notes=None, Taxes=None, ChargesAllowances=None, MonetaryAmounts=None, QuantityTotals=None, RegulatoryCompliances=None):
        super(HeaderTypeSub, self).__init__(OrderHeader, PaymentTerms, Dates, Contacts, Address, FOBRelatedInstruction, Commodity, Measurements, Paperwork, Packaging, QuantityAndWeight, CarrierInformation, CarrierSpecialHandlingDetail, MarksAndNumbersCollection, RestrictionsOrConditions, LeadTime, References, Notes, Taxes, ChargesAllowances, MonetaryAmounts, QuantityTotals, RegulatoryCompliances, )
supermod.HeaderType.subclass = HeaderTypeSub
# end class HeaderTypeSub


class OrderHeaderTypeSub(supermod.OrderHeaderType):
    def __init__(self, TradingPartnerId=None, PurchaseOrderNumber=None, DepositorOrderNumber=None, TsetPurposeCode=None, PrimaryPOTypeCode=None, PrimaryPOTypeDescription=None, AdditionalPOTypeCodes=None, ReleaseNumber=None, PurchaseOrderDate=None, PurchaseOrderTime=None, ContractType=None, SalesRequirementCode=None, AcknowledgementType=None, InvoiceTypeCode=None, ShipCompleteCode=None, BuyersCurrency=None, SellersCurrency=None, ExchangeRate=None, Department=None, DepartmentDescription=None, Vendor=None, JobNumber=None, Division=None, CustomerAccountNumber=None, CustomerOrderNumber=None, DocumentVersion=None, DocumentRevision=None):
        super(OrderHeaderTypeSub, self).__init__(TradingPartnerId, PurchaseOrderNumber, DepositorOrderNumber, TsetPurposeCode, PrimaryPOTypeCode, PrimaryPOTypeDescription, AdditionalPOTypeCodes, ReleaseNumber, PurchaseOrderDate, PurchaseOrderTime, ContractType, SalesRequirementCode, AcknowledgementType, InvoiceTypeCode, ShipCompleteCode, BuyersCurrency, SellersCurrency, ExchangeRate, Department, DepartmentDescription, Vendor, JobNumber, Division, CustomerAccountNumber, CustomerOrderNumber, DocumentVersion, DocumentRevision, )
supermod.OrderHeaderType.subclass = OrderHeaderTypeSub
# end class OrderHeaderTypeSub


class AdditionalPOTypeCodesTypeSub(supermod.AdditionalPOTypeCodesType):
    def __init__(self, POTypeCode=None, POTypeDescription=None):
        super(AdditionalPOTypeCodesTypeSub, self).__init__(POTypeCode, POTypeDescription, )
supermod.AdditionalPOTypeCodesType.subclass = AdditionalPOTypeCodesTypeSub
# end class AdditionalPOTypeCodesTypeSub


class PaymentTermsTypeSub(supermod.PaymentTermsType):
    def __init__(self, TermsType=None, TermsBasisDateCode=None, TermsTimeRelationCode=None, TermsDiscountPercentage=None, TermsDiscountDate=None, TermsDiscountDueDays=None, TermsNetDueDate=None, TermsNetDueDays=None, TermsDiscountAmount=None, TermsDeferredDueDate=None, TermsDeferredAmountDue=None, PercentOfInvoicePayable=None, TermsDescription=None, TermsDueDay=None, PaymentMethodCode=None, PaymentMethodID=None, LatePaymentChargePercent=None, TermsStartDate=None, TermsDueDateQual=None, AmountSubjectToDiscount=None, DiscountAmountDue=None):
        super(PaymentTermsTypeSub, self).__init__(TermsType, TermsBasisDateCode, TermsTimeRelationCode, TermsDiscountPercentage, TermsDiscountDate, TermsDiscountDueDays, TermsNetDueDate, TermsNetDueDays, TermsDiscountAmount, TermsDeferredDueDate, TermsDeferredAmountDue, PercentOfInvoicePayable, TermsDescription, TermsDueDay, PaymentMethodCode, PaymentMethodID, LatePaymentChargePercent, TermsStartDate, TermsDueDateQual, AmountSubjectToDiscount, DiscountAmountDue, )
supermod.PaymentTermsType.subclass = PaymentTermsTypeSub
# end class PaymentTermsTypeSub


class DatesTypeSub(supermod.DatesType):
    def __init__(self, DateTimeQualifier=None, Date=None, Time=None, DateTimePeriod=None):
        super(DatesTypeSub, self).__init__(DateTimeQualifier, Date, Time, DateTimePeriod, )
supermod.DatesType.subclass = DatesTypeSub
# end class DatesTypeSub


class ContactsTypeSub(supermod.ContactsType):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactsTypeSub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactsType.subclass = ContactsTypeSub
# end class ContactsTypeSub


class AdditionalContactDetailsTypeSub(supermod.AdditionalContactDetailsType):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsTypeSub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType.subclass = AdditionalContactDetailsTypeSub
# end class AdditionalContactDetailsTypeSub


class AddressTypeSub(supermod.AddressType):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, References=None, Contacts=None, Dates=None):
        super(AddressTypeSub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, References, Contacts, Dates, )
supermod.AddressType.subclass = AddressTypeSub
# end class AddressTypeSub


class ReferencesTypeSub(supermod.ReferencesType):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date=None, Time=None, ReferenceIDs=None):
        super(ReferencesTypeSub, self).__init__(ReferenceQual, ReferenceID, Description, Date, Time, ReferenceIDs, )
supermod.ReferencesType.subclass = ReferencesTypeSub
# end class ReferencesTypeSub


class ReferenceIDsTypeSub(supermod.ReferenceIDsType):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsTypeSub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType.subclass = ReferenceIDsTypeSub
# end class ReferenceIDsTypeSub


class ContactsType1Sub(supermod.ContactsType1):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactsType1Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactsType1.subclass = ContactsType1Sub
# end class ContactsType1Sub


class AdditionalContactDetailsType2Sub(supermod.AdditionalContactDetailsType2):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType2Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType2.subclass = AdditionalContactDetailsType2Sub
# end class AdditionalContactDetailsType2Sub


class DatesType3Sub(supermod.DatesType3):
    def __init__(self, DateTimeQualifier=None, Date=None, Time=None, DateTimePeriod=None):
        super(DatesType3Sub, self).__init__(DateTimeQualifier, Date, Time, DateTimePeriod, )
supermod.DatesType3.subclass = DatesType3Sub
# end class DatesType3Sub


class FOBRelatedInstructionTypeSub(supermod.FOBRelatedInstructionType):
    def __init__(self, FOBPayCode=None, FOBLocationQualifier=None, FOBLocationDescription=None, FOBTitlePassageCode=None, FOBTitlePassageLocation=None, TransportationTermsType=None, TransportationTerms=None, RiskOfLossCode=None, Description=None):
        super(FOBRelatedInstructionTypeSub, self).__init__(FOBPayCode, FOBLocationQualifier, FOBLocationDescription, FOBTitlePassageCode, FOBTitlePassageLocation, TransportationTermsType, TransportationTerms, RiskOfLossCode, Description, )
supermod.FOBRelatedInstructionType.subclass = FOBRelatedInstructionTypeSub
# end class FOBRelatedInstructionTypeSub


class CommodityTypeSub(supermod.CommodityType):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityTypeSub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType.subclass = CommodityTypeSub
# end class CommodityTypeSub


class MeasurementsTypeSub(supermod.MeasurementsType):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsTypeSub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType.subclass = MeasurementsTypeSub
# end class MeasurementsTypeSub


class PaperworkTypeSub(supermod.PaperworkType):
    def __init__(self, ReportTypeCode=None, ReportTransmissionCode=None, ReportCopiesNeeded=None, AddressTypeCode=None, LocationCodeQualifier=None, LocationNumber=None, Description=None, ActionsIndicated=None, RequestCategoryCode=None):
        super(PaperworkTypeSub, self).__init__(ReportTypeCode, ReportTransmissionCode, ReportCopiesNeeded, AddressTypeCode, LocationCodeQualifier, LocationNumber, Description, ActionsIndicated, RequestCategoryCode, )
supermod.PaperworkType.subclass = PaperworkTypeSub
# end class PaperworkTypeSub


class PackagingTypeSub(supermod.PackagingType):
    def __init__(self, PackagingCharacteristicCode=None, AgencyQualifierCode=None, PackagingDescriptionCode=None, PackagingDescription=None, UnitLoadOptionCode=None, Measurements=None):
        super(PackagingTypeSub, self).__init__(PackagingCharacteristicCode, AgencyQualifierCode, PackagingDescriptionCode, PackagingDescription, UnitLoadOptionCode, Measurements, )
supermod.PackagingType.subclass = PackagingTypeSub
# end class PackagingTypeSub


class MeasurementsType4Sub(supermod.MeasurementsType4):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType4Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType4.subclass = MeasurementsType4Sub
# end class MeasurementsType4Sub


class QuantityAndWeightTypeSub(supermod.QuantityAndWeightType):
    def __init__(self, PackingMedium=None, PackingMaterial=None, LadingQuantity=None, LadingDescription=None, WeightQualifier=None, Weight=None, WeightUOM=None, Volume=None, VolumeUOM=None, PalletExchangeCode=None):
        super(QuantityAndWeightTypeSub, self).__init__(PackingMedium, PackingMaterial, LadingQuantity, LadingDescription, WeightQualifier, Weight, WeightUOM, Volume, VolumeUOM, PalletExchangeCode, )
supermod.QuantityAndWeightType.subclass = QuantityAndWeightTypeSub
# end class QuantityAndWeightTypeSub


class CarrierInformationTypeSub(supermod.CarrierInformationType):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None, SealNumbers=None):
        super(CarrierInformationTypeSub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, SealNumbers, )
supermod.CarrierInformationType.subclass = CarrierInformationTypeSub
# end class CarrierInformationTypeSub


class ServiceLevelCodesTypeSub(supermod.ServiceLevelCodesType):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesTypeSub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType.subclass = ServiceLevelCodesTypeSub
# end class ServiceLevelCodesTypeSub


class AddressType5Sub(supermod.AddressType5):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Dates=None):
        super(AddressType5Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Dates, )
supermod.AddressType5.subclass = AddressType5Sub
# end class AddressType5Sub


class DatesType6Sub(supermod.DatesType6):
    def __init__(self, DateTimeQualifier=None, Date=None, Time=None, DateTimePeriod=None):
        super(DatesType6Sub, self).__init__(DateTimeQualifier, Date, Time, DateTimePeriod, )
supermod.DatesType6.subclass = DatesType6Sub
# end class DatesType6Sub


class SealNumbersTypeSub(supermod.SealNumbersType):
    def __init__(self, SealStatusCode=None, SealNumber=None):
        super(SealNumbersTypeSub, self).__init__(SealStatusCode, SealNumber, )
supermod.SealNumbersType.subclass = SealNumbersTypeSub
# end class SealNumbersTypeSub


class CarrierSpecialHandlingDetailTypeSub(supermod.CarrierSpecialHandlingDetailType):
    def __init__(self, SpecialHandlingCode=None, HazardousMaterialCode=None, HazardousMaterialClass=None, Description=None, YesOrNoResponse=None):
        super(CarrierSpecialHandlingDetailTypeSub, self).__init__(SpecialHandlingCode, HazardousMaterialCode, HazardousMaterialClass, Description, YesOrNoResponse, )
supermod.CarrierSpecialHandlingDetailType.subclass = CarrierSpecialHandlingDetailTypeSub
# end class CarrierSpecialHandlingDetailTypeSub


class MarksAndNumbersCollectionTypeSub(supermod.MarksAndNumbersCollectionType):
    def __init__(self, MarksAndNumbersQualifier1=None, MarksAndNumbers1=None):
        super(MarksAndNumbersCollectionTypeSub, self).__init__(MarksAndNumbersQualifier1, MarksAndNumbers1, )
supermod.MarksAndNumbersCollectionType.subclass = MarksAndNumbersCollectionTypeSub
# end class MarksAndNumbersCollectionTypeSub


class RestrictionsOrConditionsTypeSub(supermod.RestrictionsOrConditionsType):
    def __init__(self, RestrictionsConditionsQualifier=None, Description=None, QuantityQualifier=None, Quantity1=None, AmountQualifier=None, Amount=None):
        super(RestrictionsOrConditionsTypeSub, self).__init__(RestrictionsConditionsQualifier, Description, QuantityQualifier, Quantity1, AmountQualifier, Amount, )
supermod.RestrictionsOrConditionsType.subclass = RestrictionsOrConditionsTypeSub
# end class RestrictionsOrConditionsTypeSub


class LeadTimeTypeSub(supermod.LeadTimeType):
    def __init__(self, LeadTimeCode=None, LeadTimeQuantity=None, LeadTimePeriodInterval=None, LeadTimeDate=None, References=None, Notes=None):
        super(LeadTimeTypeSub, self).__init__(LeadTimeCode, LeadTimeQuantity, LeadTimePeriodInterval, LeadTimeDate, References, Notes, )
supermod.LeadTimeType.subclass = LeadTimeTypeSub
# end class LeadTimeTypeSub


class ReferencesType7Sub(supermod.ReferencesType7):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date=None, Time=None, ReferenceIDs=None):
        super(ReferencesType7Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date, Time, ReferenceIDs, )
supermod.ReferencesType7.subclass = ReferencesType7Sub
# end class ReferencesType7Sub


class ReferenceIDsType8Sub(supermod.ReferenceIDsType8):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType8Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType8.subclass = ReferenceIDsType8Sub
# end class ReferenceIDsType8Sub


class NotesTypeSub(supermod.NotesType):
    def __init__(self, NoteCode=None, Note=None, LanguageCode=None):
        super(NotesTypeSub, self).__init__(NoteCode, Note, LanguageCode, )
supermod.NotesType.subclass = NotesTypeSub
# end class NotesTypeSub


class ReferencesType9Sub(supermod.ReferencesType9):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date=None, Time=None, ReferenceIDs=None):
        super(ReferencesType9Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date, Time, ReferenceIDs, )
supermod.ReferencesType9.subclass = ReferencesType9Sub
# end class ReferencesType9Sub


class ReferenceIDsType10Sub(supermod.ReferenceIDsType10):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType10Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType10.subclass = ReferenceIDsType10Sub
# end class ReferenceIDsType10Sub


class NotesType11Sub(supermod.NotesType11):
    def __init__(self, NoteCode=None, Note=None, LanguageCode=None):
        super(NotesType11Sub, self).__init__(NoteCode, Note, LanguageCode, )
supermod.NotesType11.subclass = NotesType11Sub
# end class NotesType11Sub


class TaxesTypeSub(supermod.TaxesType):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PercentDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxesTypeSub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PercentDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxesType.subclass = TaxesTypeSub
# end class TaxesTypeSub


class ChargesAllowancesTypeSub(supermod.ChargesAllowancesType):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, CalculationSequence=None, Taxes=None):
        super(ChargesAllowancesTypeSub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, CalculationSequence, Taxes, )
supermod.ChargesAllowancesType.subclass = ChargesAllowancesTypeSub
# end class ChargesAllowancesTypeSub


class TaxesType12Sub(supermod.TaxesType12):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PercentDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxesType12Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PercentDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxesType12.subclass = TaxesType12Sub
# end class TaxesType12Sub


class MonetaryAmountsTypeSub(supermod.MonetaryAmountsType):
    def __init__(self, MonetaryAmountCode=None, MonetaryAmount=None, CreditDebitFlag=None):
        super(MonetaryAmountsTypeSub, self).__init__(MonetaryAmountCode, MonetaryAmount, CreditDebitFlag, )
supermod.MonetaryAmountsType.subclass = MonetaryAmountsTypeSub
# end class MonetaryAmountsTypeSub


class QuantityTotalsTypeSub(supermod.QuantityTotalsType):
    def __init__(self, QuantityTotalsQualifier=None, Quantity=None, QuantityUOM=None, WeightQualifier=None, Weight=None, WeightUOM=None, Volume=None, VolumeUOM=None, Description=None):
        super(QuantityTotalsTypeSub, self).__init__(QuantityTotalsQualifier, Quantity, QuantityUOM, WeightQualifier, Weight, WeightUOM, Volume, VolumeUOM, Description, )
supermod.QuantityTotalsType.subclass = QuantityTotalsTypeSub
# end class QuantityTotalsTypeSub


class RegulatoryCompliancesTypeSub(supermod.RegulatoryCompliancesType):
    def __init__(self, RegulatoryComplianceQual=None, YesOrNoResponse=None, RegulatoryComplianceID=None, RegulatoryAgency=None, Description=None):
        super(RegulatoryCompliancesTypeSub, self).__init__(RegulatoryComplianceQual, YesOrNoResponse, RegulatoryComplianceID, RegulatoryAgency, Description, )
supermod.RegulatoryCompliancesType.subclass = RegulatoryCompliancesTypeSub
# end class RegulatoryCompliancesTypeSub


class LineItemTypeSub(supermod.LineItemType):
    def __init__(self, OrderLine=None, Contacts=None, Dates=None, Measurements=None, PriceInformation=None, ProductOrItemDescription=None, MasterItemAttribute=None, Paperwork=None, PhysicalDetails=None, PalletInformation=None, References=None, Notes=None, FloorReady=None, Address=None, Subline=None, QuantitiesSchedulesLocations=None, Taxes=None, ChargesAllowances=None, PaymentTerms=None, ConditionOfSale=None, FOBRelatedInstruction=None, Commodity=None, CarrierInformation=None, CarrierSpecialHandlingDetail=None, MarksAndNumbersCollection=None, RestrictionsOrConditions=None, Packaging=None, MonetaryAmounts=None, RegulatoryCompliances=None):
        super(LineItemTypeSub, self).__init__(OrderLine, Contacts, Dates, Measurements, PriceInformation, ProductOrItemDescription, MasterItemAttribute, Paperwork, PhysicalDetails, PalletInformation, References, Notes, FloorReady, Address, Subline, QuantitiesSchedulesLocations, Taxes, ChargesAllowances, PaymentTerms, ConditionOfSale, FOBRelatedInstruction, Commodity, CarrierInformation, CarrierSpecialHandlingDetail, MarksAndNumbersCollection, RestrictionsOrConditions, Packaging, MonetaryAmounts, RegulatoryCompliances, )
supermod.LineItemType.subclass = LineItemTypeSub
# end class LineItemTypeSub


class OrderLineTypeSub(supermod.OrderLineType):
    def __init__(self, LineSequenceNumber=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None, OrderQty=None, OrderQtyUOM=None, PurchasePriceType=None, PurchasePrice=None, PurchasePriceBasis=None, BuyersCurrency=None, SellersCurrency=None, ExchangeRate=None, ShipDate=None, ExtendedItemTotal=None, ProductSizeCode=None, ProductSizeDescription=None, ProductColorCode=None, ProductColorDescription=None, ProductMaterialCode=None, ProductMaterialDescription=None, ProductProcessCode=None, ProductProcessDescription=None, Department=None, DepartmentDescription=None, Class=None, Gender=None, SellerDateCode=None, NRFStandardColorAndSize=None):
        super(OrderLineTypeSub, self).__init__(LineSequenceNumber, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, OrderQty, OrderQtyUOM, PurchasePriceType, PurchasePrice, PurchasePriceBasis, BuyersCurrency, SellersCurrency, ExchangeRate, ShipDate, ExtendedItemTotal, ProductSizeCode, ProductSizeDescription, ProductColorCode, ProductColorDescription, ProductMaterialCode, ProductMaterialDescription, ProductProcessCode, ProductProcessDescription, Department, DepartmentDescription, Class, Gender, SellerDateCode, NRFStandardColorAndSize, )
supermod.OrderLineType.subclass = OrderLineTypeSub
# end class OrderLineTypeSub


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


class ContactsType13Sub(supermod.ContactsType13):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactsType13Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactsType13.subclass = ContactsType13Sub
# end class ContactsType13Sub


class AdditionalContactDetailsType14Sub(supermod.AdditionalContactDetailsType14):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType14Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType14.subclass = AdditionalContactDetailsType14Sub
# end class AdditionalContactDetailsType14Sub


class DatesType15Sub(supermod.DatesType15):
    def __init__(self, DateTimeQualifier=None, Date=None, Time=None, DateTimePeriod=None):
        super(DatesType15Sub, self).__init__(DateTimeQualifier, Date, Time, DateTimePeriod, )
supermod.DatesType15.subclass = DatesType15Sub
# end class DatesType15Sub


class MeasurementsType16Sub(supermod.MeasurementsType16):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType16Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType16.subclass = MeasurementsType16Sub
# end class MeasurementsType16Sub


class PriceInformationTypeSub(supermod.PriceInformationType):
    def __init__(self, ChangeReasonCode=None, EffectiveDate=None, PriceTypeIDCode=None, UnitPrice=None, UnitPriceBasis=None, UnitPriceBasisMultiplier=None, Currency=None, PriceMultiplierQual=None, PriceMultiplier=None, RebateAmount=None, Quantity=None, QuantityUOM=None, MultiplePriceQuantity=None, ClassOfTradeCode=None, ConditionValue=None, Description=None):
        super(PriceInformationTypeSub, self).__init__(ChangeReasonCode, EffectiveDate, PriceTypeIDCode, UnitPrice, UnitPriceBasis, UnitPriceBasisMultiplier, Currency, PriceMultiplierQual, PriceMultiplier, RebateAmount, Quantity, QuantityUOM, MultiplePriceQuantity, ClassOfTradeCode, ConditionValue, Description, )
supermod.PriceInformationType.subclass = PriceInformationTypeSub
# end class PriceInformationTypeSub


class ProductOrItemDescriptionTypeSub(supermod.ProductOrItemDescriptionType):
    def __init__(self, ProductCharacteristicCode=None, AgencyQualifierCode=None, ProductDescriptionCode=None, ProductDescription=None, SurfaceLayerPositionCode=None, SourceSubqualifier=None, YesOrNoResponse=None, LanguageCode=None):
        super(ProductOrItemDescriptionTypeSub, self).__init__(ProductCharacteristicCode, AgencyQualifierCode, ProductDescriptionCode, ProductDescription, SurfaceLayerPositionCode, SourceSubqualifier, YesOrNoResponse, LanguageCode, )
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


class MeasurementsType17Sub(supermod.MeasurementsType17):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType17Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType17.subclass = MeasurementsType17Sub
# end class MeasurementsType17Sub


class PaperworkType18Sub(supermod.PaperworkType18):
    def __init__(self, ReportTypeCode=None, ReportTransmissionCode=None, ReportCopiesNeeded=None, AddressTypeCode=None, LocationCodeQualifier=None, LocationNumber=None, Description=None, ActionsIndicated=None, RequestCategoryCode=None):
        super(PaperworkType18Sub, self).__init__(ReportTypeCode, ReportTransmissionCode, ReportCopiesNeeded, AddressTypeCode, LocationCodeQualifier, LocationNumber, Description, ActionsIndicated, RequestCategoryCode, )
supermod.PaperworkType18.subclass = PaperworkType18Sub
# end class PaperworkType18Sub


class PhysicalDetailsTypeSub(supermod.PhysicalDetailsType):
    def __init__(self, PackQualifier=None, PackValue=None, PackSize=None, PackUOM=None, PackingMedium=None, PackingMaterial=None, WeightQualifier=None, PackWeight=None, PackWeightUOM=None, PackVolume=None, PackVolumeUOM=None, PackLength=None, PackWidth=None, PackHeight=None, DimensionUOM=None, Description=None, SurfaceLayerPositionCode=None, AssignedID=None):
        super(PhysicalDetailsTypeSub, self).__init__(PackQualifier, PackValue, PackSize, PackUOM, PackingMedium, PackingMaterial, WeightQualifier, PackWeight, PackWeightUOM, PackVolume, PackVolumeUOM, PackLength, PackWidth, PackHeight, DimensionUOM, Description, SurfaceLayerPositionCode, AssignedID, )
supermod.PhysicalDetailsType.subclass = PhysicalDetailsTypeSub
# end class PhysicalDetailsTypeSub


class PalletInformationTypeSub(supermod.PalletInformationType):
    def __init__(self, PalletQualifier=None, PalletValue=None, PalletTypeCode=None, PalletTiers=None, PalletBlocks=None, UnitWeight=None, UnitWeightUOM=None, Length=None, Width=None, Height=None, DimensionUOM=None, WeightQualifier=None, PalletWeight=None, PalletWeightUOM=None, PalletVolume=None, PalletVolumeUOM=None, UnloadedHeight=None, UnloadedHeightUOM=None, PalletExchangeCode=None, PalletStructureCode=None):
        super(PalletInformationTypeSub, self).__init__(PalletQualifier, PalletValue, PalletTypeCode, PalletTiers, PalletBlocks, UnitWeight, UnitWeightUOM, Length, Width, Height, DimensionUOM, WeightQualifier, PalletWeight, PalletWeightUOM, PalletVolume, PalletVolumeUOM, UnloadedHeight, UnloadedHeightUOM, PalletExchangeCode, PalletStructureCode, )
supermod.PalletInformationType.subclass = PalletInformationTypeSub
# end class PalletInformationTypeSub


class ReferencesType19Sub(supermod.ReferencesType19):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date=None, Time=None, ReferenceIDs=None):
        super(ReferencesType19Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date, Time, ReferenceIDs, )
supermod.ReferencesType19.subclass = ReferencesType19Sub
# end class ReferencesType19Sub


class ReferenceIDsType20Sub(supermod.ReferenceIDsType20):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType20Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType20.subclass = ReferenceIDsType20Sub
# end class ReferenceIDsType20Sub


class NotesType21Sub(supermod.NotesType21):
    def __init__(self, NoteCode=None, Note=None, LanguageCode=None):
        super(NotesType21Sub, self).__init__(NoteCode, Note, LanguageCode, )
supermod.NotesType21.subclass = NotesType21Sub
# end class NotesType21Sub


class FloorReadyTypeSub(supermod.FloorReadyType):
    def __init__(self, FloorReadyRequired=None, FloorReadyTypeCode=None, FloorReadyDescription=None, FloorReadyID=None):
        super(FloorReadyTypeSub, self).__init__(FloorReadyRequired, FloorReadyTypeCode, FloorReadyDescription, FloorReadyID, )
supermod.FloorReadyType.subclass = FloorReadyTypeSub
# end class FloorReadyTypeSub


class AddressType22Sub(supermod.AddressType22):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, References=None, Contacts=None, Dates=None):
        super(AddressType22Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, References, Contacts, Dates, )
supermod.AddressType22.subclass = AddressType22Sub
# end class AddressType22Sub


class ReferencesType23Sub(supermod.ReferencesType23):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date=None, Time=None, ReferenceIDs=None):
        super(ReferencesType23Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date, Time, ReferenceIDs, )
supermod.ReferencesType23.subclass = ReferencesType23Sub
# end class ReferencesType23Sub


class ReferenceIDsType24Sub(supermod.ReferenceIDsType24):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType24Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType24.subclass = ReferenceIDsType24Sub
# end class ReferenceIDsType24Sub


class ContactsType25Sub(supermod.ContactsType25):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactsType25Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactsType25.subclass = ContactsType25Sub
# end class ContactsType25Sub


class AdditionalContactDetailsType26Sub(supermod.AdditionalContactDetailsType26):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType26Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType26.subclass = AdditionalContactDetailsType26Sub
# end class AdditionalContactDetailsType26Sub


class DatesType27Sub(supermod.DatesType27):
    def __init__(self, DateTimeQualifier=None, Date=None, Time=None, DateTimePeriod=None):
        super(DatesType27Sub, self).__init__(DateTimeQualifier, Date, Time, DateTimePeriod, )
supermod.DatesType27.subclass = DatesType27Sub
# end class DatesType27Sub


class SublineTypeSub(supermod.SublineType):
    def __init__(self, SublineItemDetail=None, Dates=None, PriceInformation=None, ProductOrItemDescription=None, PhysicalDetails=None, References=None, Notes=None, FloorReady=None, Taxes=None, ChargesAllowances=None, Address=None, Commodity=None, RegulatoryCompliances=None):
        super(SublineTypeSub, self).__init__(SublineItemDetail, Dates, PriceInformation, ProductOrItemDescription, PhysicalDetails, References, Notes, FloorReady, Taxes, ChargesAllowances, Address, Commodity, RegulatoryCompliances, )
supermod.SublineType.subclass = SublineTypeSub
# end class SublineTypeSub


class SublineItemDetailTypeSub(supermod.SublineItemDetailType):
    def __init__(self, LineSequenceNumber=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None, ProductSizeCode=None, ProductSizeDescription=None, ProductColorCode=None, ProductColorDescription=None, ProductMaterialCode=None, ProductMaterialDescription=None, ProductProcessCode=None, ProductProcessDescription=None, QtyPer=None, QtyPerUOM=None, PurchasePriceType=None, PurchasePrice=None, PurchasePriceBasis=None, Gender=None, NRFStandardColorAndSize=None):
        super(SublineItemDetailTypeSub, self).__init__(LineSequenceNumber, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, ProductSizeCode, ProductSizeDescription, ProductColorCode, ProductColorDescription, ProductMaterialCode, ProductMaterialDescription, ProductProcessCode, ProductProcessDescription, QtyPer, QtyPerUOM, PurchasePriceType, PurchasePrice, PurchasePriceBasis, Gender, NRFStandardColorAndSize, )
supermod.SublineItemDetailType.subclass = SublineItemDetailTypeSub
# end class SublineItemDetailTypeSub


class ProductIDType28Sub(supermod.ProductIDType28):
    def __init__(self, PartNumberQual=None, PartNumber=None):
        super(ProductIDType28Sub, self).__init__(PartNumberQual, PartNumber, )
supermod.ProductIDType28.subclass = ProductIDType28Sub
# end class ProductIDType28Sub


class NRFStandardColorAndSizeType29Sub(supermod.NRFStandardColorAndSizeType29):
    def __init__(self, NRFColorCode=None, ColorCategoryName=None, ColorPrimaryDescription=None, NRFSizeCode=None, SizeCategoryName=None, SizePrimaryDescription=None, SizeSecondaryDescription=None, SizeTableName=None, SizeHeading1=None, SizeHeading2=None, SizeHeading3=None, SizeHeading4=None):
        super(NRFStandardColorAndSizeType29Sub, self).__init__(NRFColorCode, ColorCategoryName, ColorPrimaryDescription, NRFSizeCode, SizeCategoryName, SizePrimaryDescription, SizeSecondaryDescription, SizeTableName, SizeHeading1, SizeHeading2, SizeHeading3, SizeHeading4, )
supermod.NRFStandardColorAndSizeType29.subclass = NRFStandardColorAndSizeType29Sub
# end class NRFStandardColorAndSizeType29Sub


class DatesType30Sub(supermod.DatesType30):
    def __init__(self, DateTimeQualifier=None, Date=None, Time=None, DateTimePeriod=None):
        super(DatesType30Sub, self).__init__(DateTimeQualifier, Date, Time, DateTimePeriod, )
supermod.DatesType30.subclass = DatesType30Sub
# end class DatesType30Sub


class PriceInformationType31Sub(supermod.PriceInformationType31):
    def __init__(self, ChangeReasonCode=None, EffectiveDate=None, PriceTypeIDCode=None, UnitPrice=None, UnitPriceBasis=None, UnitPriceBasisMultiplier=None, Currency=None, PriceMultiplierQual=None, PriceMultiplier=None, RebateAmount=None, Quantity=None, QuantityUOM=None, MultiplePriceQuantity=None, ClassOfTradeCode=None, ConditionValue=None, Description=None):
        super(PriceInformationType31Sub, self).__init__(ChangeReasonCode, EffectiveDate, PriceTypeIDCode, UnitPrice, UnitPriceBasis, UnitPriceBasisMultiplier, Currency, PriceMultiplierQual, PriceMultiplier, RebateAmount, Quantity, QuantityUOM, MultiplePriceQuantity, ClassOfTradeCode, ConditionValue, Description, )
supermod.PriceInformationType31.subclass = PriceInformationType31Sub
# end class PriceInformationType31Sub


class ProductOrItemDescriptionType32Sub(supermod.ProductOrItemDescriptionType32):
    def __init__(self, ProductCharacteristicCode=None, AgencyQualifierCode=None, ProductDescriptionCode=None, ProductDescription=None, SurfaceLayerPositionCode=None, SourceSubqualifier=None, YesOrNoResponse=None, LanguageCode=None):
        super(ProductOrItemDescriptionType32Sub, self).__init__(ProductCharacteristicCode, AgencyQualifierCode, ProductDescriptionCode, ProductDescription, SurfaceLayerPositionCode, SourceSubqualifier, YesOrNoResponse, LanguageCode, )
supermod.ProductOrItemDescriptionType32.subclass = ProductOrItemDescriptionType32Sub
# end class ProductOrItemDescriptionType32Sub


class PhysicalDetailsType33Sub(supermod.PhysicalDetailsType33):
    def __init__(self, PackQualifier=None, PackValue=None, PackSize=None, PackUOM=None, PackingMedium=None, PackingMaterial=None, WeightQualifier=None, PackWeight=None, PackWeightUOM=None, PackVolume=None, PackVolumeUOM=None, PackLength=None, PackWidth=None, PackHeight=None, DimensionUOM=None, Description=None, SurfaceLayerPositionCode=None, AssignedID=None):
        super(PhysicalDetailsType33Sub, self).__init__(PackQualifier, PackValue, PackSize, PackUOM, PackingMedium, PackingMaterial, WeightQualifier, PackWeight, PackWeightUOM, PackVolume, PackVolumeUOM, PackLength, PackWidth, PackHeight, DimensionUOM, Description, SurfaceLayerPositionCode, AssignedID, )
supermod.PhysicalDetailsType33.subclass = PhysicalDetailsType33Sub
# end class PhysicalDetailsType33Sub


class ReferencesType34Sub(supermod.ReferencesType34):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date=None, Time=None, ReferenceIDs=None):
        super(ReferencesType34Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date, Time, ReferenceIDs, )
supermod.ReferencesType34.subclass = ReferencesType34Sub
# end class ReferencesType34Sub


class ReferenceIDsType35Sub(supermod.ReferenceIDsType35):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType35Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType35.subclass = ReferenceIDsType35Sub
# end class ReferenceIDsType35Sub


class NotesType36Sub(supermod.NotesType36):
    def __init__(self, NoteCode=None, Note=None, LanguageCode=None):
        super(NotesType36Sub, self).__init__(NoteCode, Note, LanguageCode, )
supermod.NotesType36.subclass = NotesType36Sub
# end class NotesType36Sub


class FloorReadyType37Sub(supermod.FloorReadyType37):
    def __init__(self, FloorReadyRequired=None, FloorReadyTypeCode=None, FloorReadyDescription=None, FloorReadyID=None):
        super(FloorReadyType37Sub, self).__init__(FloorReadyRequired, FloorReadyTypeCode, FloorReadyDescription, FloorReadyID, )
supermod.FloorReadyType37.subclass = FloorReadyType37Sub
# end class FloorReadyType37Sub


class TaxesType38Sub(supermod.TaxesType38):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PercentDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxesType38Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PercentDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxesType38.subclass = TaxesType38Sub
# end class TaxesType38Sub


class ChargesAllowancesType39Sub(supermod.ChargesAllowancesType39):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, CalculationSequence=None, Taxes=None):
        super(ChargesAllowancesType39Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, CalculationSequence, Taxes, )
supermod.ChargesAllowancesType39.subclass = ChargesAllowancesType39Sub
# end class ChargesAllowancesType39Sub


class TaxesType40Sub(supermod.TaxesType40):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PercentDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxesType40Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PercentDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxesType40.subclass = TaxesType40Sub
# end class TaxesType40Sub


class AddressType41Sub(supermod.AddressType41):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, References=None, Contacts=None, Dates=None):
        super(AddressType41Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, References, Contacts, Dates, )
supermod.AddressType41.subclass = AddressType41Sub
# end class AddressType41Sub


class ReferencesType42Sub(supermod.ReferencesType42):
    def __init__(self, ReferenceQual=None, ReferenceID=None, Description=None, Date=None, Time=None, ReferenceIDs=None):
        super(ReferencesType42Sub, self).__init__(ReferenceQual, ReferenceID, Description, Date, Time, ReferenceIDs, )
supermod.ReferencesType42.subclass = ReferencesType42Sub
# end class ReferencesType42Sub


class ReferenceIDsType43Sub(supermod.ReferenceIDsType43):
    def __init__(self, ReferenceQual=None, ReferenceID=None):
        super(ReferenceIDsType43Sub, self).__init__(ReferenceQual, ReferenceID, )
supermod.ReferenceIDsType43.subclass = ReferenceIDsType43Sub
# end class ReferenceIDsType43Sub


class ContactsType44Sub(supermod.ContactsType44):
    def __init__(self, ContactTypeCode=None, ContactName=None, PrimaryPhone=None, PrimaryFax=None, PrimaryEmail=None, AdditionalContactDetails=None, ContactReference=None):
        super(ContactsType44Sub, self).__init__(ContactTypeCode, ContactName, PrimaryPhone, PrimaryFax, PrimaryEmail, AdditionalContactDetails, ContactReference, )
supermod.ContactsType44.subclass = ContactsType44Sub
# end class ContactsType44Sub


class AdditionalContactDetailsType45Sub(supermod.AdditionalContactDetailsType45):
    def __init__(self, ContactQual=None, ContactID=None):
        super(AdditionalContactDetailsType45Sub, self).__init__(ContactQual, ContactID, )
supermod.AdditionalContactDetailsType45.subclass = AdditionalContactDetailsType45Sub
# end class AdditionalContactDetailsType45Sub


class DatesType46Sub(supermod.DatesType46):
    def __init__(self, DateTimeQualifier=None, Date=None, Time=None, DateTimePeriod=None):
        super(DatesType46Sub, self).__init__(DateTimeQualifier, Date, Time, DateTimePeriod, )
supermod.DatesType46.subclass = DatesType46Sub
# end class DatesType46Sub


class CommodityType47Sub(supermod.CommodityType47):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType47Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType47.subclass = CommodityType47Sub
# end class CommodityType47Sub


class RegulatoryCompliancesType48Sub(supermod.RegulatoryCompliancesType48):
    def __init__(self, RegulatoryComplianceQual=None, YesOrNoResponse=None, RegulatoryComplianceID=None, RegulatoryAgency=None, Description=None):
        super(RegulatoryCompliancesType48Sub, self).__init__(RegulatoryComplianceQual, YesOrNoResponse, RegulatoryComplianceID, RegulatoryAgency, Description, )
supermod.RegulatoryCompliancesType48.subclass = RegulatoryCompliancesType48Sub
# end class RegulatoryCompliancesType48Sub


class QuantitiesSchedulesLocationsTypeSub(supermod.QuantitiesSchedulesLocationsType):
    def __init__(self, QuantityQualifier=None, TotalQty=None, TotalQtyUOM=None, QuantityDescription=None, LocationCodeQualifier=None, LocationDescription=None, LocationQuantity=None, Dates=None, AssignedID=None, LeadTimeCode=None, LeadTimeQuantity=None, LeadTimePeriodInterval=None, LeadTimeDate=None):
        super(QuantitiesSchedulesLocationsTypeSub, self).__init__(QuantityQualifier, TotalQty, TotalQtyUOM, QuantityDescription, LocationCodeQualifier, LocationDescription, LocationQuantity, Dates, AssignedID, LeadTimeCode, LeadTimeQuantity, LeadTimePeriodInterval, LeadTimeDate, )
supermod.QuantitiesSchedulesLocationsType.subclass = QuantitiesSchedulesLocationsTypeSub
# end class QuantitiesSchedulesLocationsTypeSub


class LocationQuantityTypeSub(supermod.LocationQuantityType):
    def __init__(self, Location=None, Qty=None):
        super(LocationQuantityTypeSub, self).__init__(Location, Qty, )
supermod.LocationQuantityType.subclass = LocationQuantityTypeSub
# end class LocationQuantityTypeSub


class DatesType49Sub(supermod.DatesType49):
    def __init__(self, DateTimeQualifier=None, Date=None, Time=None, DateTimePeriod=None):
        super(DatesType49Sub, self).__init__(DateTimeQualifier, Date, Time, DateTimePeriod, )
supermod.DatesType49.subclass = DatesType49Sub
# end class DatesType49Sub


class TaxesType50Sub(supermod.TaxesType50):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PercentDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxesType50Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PercentDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxesType50.subclass = TaxesType50Sub
# end class TaxesType50Sub


class ChargesAllowancesType51Sub(supermod.ChargesAllowancesType51):
    def __init__(self, AllowChrgIndicator=None, AllowChrgCode=None, AllowChrgAgencyCode=None, AllowChrgAgency=None, AllowChrgAmt=None, AllowChrgPercentQual=None, AllowChrgPercent=None, PercentDollarBasis=None, AllowChrgRate=None, AllowChrgQtyUOM=None, AllowChrgQty=None, AllowChrgHandlingCode=None, ReferenceIdentification=None, AllowChrgHandlingDescription=None, OptionNumber=None, ExceptionNumber=None, AllowChrgQty2=None, LanguageCode=None, CalculationSequence=None, Taxes=None):
        super(ChargesAllowancesType51Sub, self).__init__(AllowChrgIndicator, AllowChrgCode, AllowChrgAgencyCode, AllowChrgAgency, AllowChrgAmt, AllowChrgPercentQual, AllowChrgPercent, PercentDollarBasis, AllowChrgRate, AllowChrgQtyUOM, AllowChrgQty, AllowChrgHandlingCode, ReferenceIdentification, AllowChrgHandlingDescription, OptionNumber, ExceptionNumber, AllowChrgQty2, LanguageCode, CalculationSequence, Taxes, )
supermod.ChargesAllowancesType51.subclass = ChargesAllowancesType51Sub
# end class ChargesAllowancesType51Sub


class TaxesType52Sub(supermod.TaxesType52):
    def __init__(self, TaxTypeCode=None, TaxAmount=None, TaxPercentQual=None, TaxPercent=None, JurisdictionQual=None, JurisdictionCode=None, TaxExemptCode=None, RelationshipCode=None, PercentDollarBasis=None, TaxHandlingCode=None, TaxID=None, AssignedID=None, Description=None):
        super(TaxesType52Sub, self).__init__(TaxTypeCode, TaxAmount, TaxPercentQual, TaxPercent, JurisdictionQual, JurisdictionCode, TaxExemptCode, RelationshipCode, PercentDollarBasis, TaxHandlingCode, TaxID, AssignedID, Description, )
supermod.TaxesType52.subclass = TaxesType52Sub
# end class TaxesType52Sub


class PaymentTermsType53Sub(supermod.PaymentTermsType53):
    def __init__(self, TermsType=None, TermsBasisDateCode=None, TermsTimeRelationCode=None, TermsDiscountPercentage=None, TermsDiscountDate=None, TermsDiscountDueDays=None, TermsNetDueDate=None, TermsNetDueDays=None, TermsDiscountAmount=None, TermsDeferredDueDate=None, TermsDeferredAmountDue=None, PercentOfInvoicePayable=None, TermsDescription=None, TermsDueDay=None, PaymentMethodCode=None, PaymentMethodID=None, LatePaymentChargePercent=None, TermsStartDate=None, TermsDueDateQual=None, AmountSubjectToDiscount=None, DiscountAmountDue=None):
        super(PaymentTermsType53Sub, self).__init__(TermsType, TermsBasisDateCode, TermsTimeRelationCode, TermsDiscountPercentage, TermsDiscountDate, TermsDiscountDueDays, TermsNetDueDate, TermsNetDueDays, TermsDiscountAmount, TermsDeferredDueDate, TermsDeferredAmountDue, PercentOfInvoicePayable, TermsDescription, TermsDueDay, PaymentMethodCode, PaymentMethodID, LatePaymentChargePercent, TermsStartDate, TermsDueDateQual, AmountSubjectToDiscount, DiscountAmountDue, )
supermod.PaymentTermsType53.subclass = PaymentTermsType53Sub
# end class PaymentTermsType53Sub


class ConditionOfSaleTypeSub(supermod.ConditionOfSaleType):
    def __init__(self, LineSequenceNumber=None, SalesRequirementCode=None, ActionCode=None, Amount=None, AccountNumber=None, Date=None, AgencyQualifierCode=None, SubstitutionCode=None, ApplicationId=None, BuyerPartNumber=None, VendorPartNumber=None, ConsumerPackageCode=None, EAN=None, GTIN=None, UPCCaseCode=None, NatlDrugCode=None, InternationalStandardBookNumber=None, ProductID=None):
        super(ConditionOfSaleTypeSub, self).__init__(LineSequenceNumber, SalesRequirementCode, ActionCode, Amount, AccountNumber, Date, AgencyQualifierCode, SubstitutionCode, ApplicationId, BuyerPartNumber, VendorPartNumber, ConsumerPackageCode, EAN, GTIN, UPCCaseCode, NatlDrugCode, InternationalStandardBookNumber, ProductID, )
supermod.ConditionOfSaleType.subclass = ConditionOfSaleTypeSub
# end class ConditionOfSaleTypeSub


class ProductIDType54Sub(supermod.ProductIDType54):
    def __init__(self, PartNumberQual=None, PartNumber=None):
        super(ProductIDType54Sub, self).__init__(PartNumberQual, PartNumber, )
supermod.ProductIDType54.subclass = ProductIDType54Sub
# end class ProductIDType54Sub


class FOBRelatedInstructionType55Sub(supermod.FOBRelatedInstructionType55):
    def __init__(self, FOBPayCode=None, FOBLocationQualifier=None, FOBLocationDescription=None, FOBTitlePassageCode=None, FOBTitlePassageLocation=None, TransportationTermsType=None, TransportationTerms=None, RiskOfLossCode=None, Description=None):
        super(FOBRelatedInstructionType55Sub, self).__init__(FOBPayCode, FOBLocationQualifier, FOBLocationDescription, FOBTitlePassageCode, FOBTitlePassageLocation, TransportationTermsType, TransportationTerms, RiskOfLossCode, Description, )
supermod.FOBRelatedInstructionType55.subclass = FOBRelatedInstructionType55Sub
# end class FOBRelatedInstructionType55Sub


class CommodityType56Sub(supermod.CommodityType56):
    def __init__(self, CommodityCodeQualifier=None, CommodityCode=None):
        super(CommodityType56Sub, self).__init__(CommodityCodeQualifier, CommodityCode, )
supermod.CommodityType56.subclass = CommodityType56Sub
# end class CommodityType56Sub


class CarrierInformationType57Sub(supermod.CarrierInformationType57):
    def __init__(self, StatusCode=None, CarrierTransMethodCode=None, CarrierAlphaCode=None, CarrierRouting=None, EquipmentDescriptionCode=None, CarrierEquipmentInitial=None, CarrierEquipmentNumber=None, EquipmentType=None, OwnershipCode=None, RoutingSequenceCode=None, TransitDirectionCode=None, TransitTimeQual=None, TransitTime=None, ServiceLevelCodes=None, Address=None, SealNumbers=None):
        super(CarrierInformationType57Sub, self).__init__(StatusCode, CarrierTransMethodCode, CarrierAlphaCode, CarrierRouting, EquipmentDescriptionCode, CarrierEquipmentInitial, CarrierEquipmentNumber, EquipmentType, OwnershipCode, RoutingSequenceCode, TransitDirectionCode, TransitTimeQual, TransitTime, ServiceLevelCodes, Address, SealNumbers, )
supermod.CarrierInformationType57.subclass = CarrierInformationType57Sub
# end class CarrierInformationType57Sub


class ServiceLevelCodesType58Sub(supermod.ServiceLevelCodesType58):
    def __init__(self, ServiceLevelCode=None):
        super(ServiceLevelCodesType58Sub, self).__init__(ServiceLevelCode, )
supermod.ServiceLevelCodesType58.subclass = ServiceLevelCodesType58Sub
# end class ServiceLevelCodesType58Sub


class AddressType59Sub(supermod.AddressType59):
    def __init__(self, AddressTypeCode=None, LocationCodeQualifier=None, AddressLocationNumber=None, AddressName=None, AddressAlternateName=None, AddressAlternateName2=None, Address1=None, Address2=None, Address3=None, Address4=None, City=None, State=None, PostalCode=None, Country=None, LocationID=None, CountrySubDivision=None, AddressTaxIdNumber=None, AddressTaxExemptNumber=None, Dates=None):
        super(AddressType59Sub, self).__init__(AddressTypeCode, LocationCodeQualifier, AddressLocationNumber, AddressName, AddressAlternateName, AddressAlternateName2, Address1, Address2, Address3, Address4, City, State, PostalCode, Country, LocationID, CountrySubDivision, AddressTaxIdNumber, AddressTaxExemptNumber, Dates, )
supermod.AddressType59.subclass = AddressType59Sub
# end class AddressType59Sub


class DatesType60Sub(supermod.DatesType60):
    def __init__(self, DateTimeQualifier=None, Date=None, Time=None, DateTimePeriod=None):
        super(DatesType60Sub, self).__init__(DateTimeQualifier, Date, Time, DateTimePeriod, )
supermod.DatesType60.subclass = DatesType60Sub
# end class DatesType60Sub


class SealNumbersType61Sub(supermod.SealNumbersType61):
    def __init__(self, SealStatusCode=None, SealNumber=None):
        super(SealNumbersType61Sub, self).__init__(SealStatusCode, SealNumber, )
supermod.SealNumbersType61.subclass = SealNumbersType61Sub
# end class SealNumbersType61Sub


class CarrierSpecialHandlingDetailType62Sub(supermod.CarrierSpecialHandlingDetailType62):
    def __init__(self, SpecialHandlingCode=None, HazardousMaterialCode=None, HazardousMaterialClass=None, Description=None, YesOrNoResponse=None):
        super(CarrierSpecialHandlingDetailType62Sub, self).__init__(SpecialHandlingCode, HazardousMaterialCode, HazardousMaterialClass, Description, YesOrNoResponse, )
supermod.CarrierSpecialHandlingDetailType62.subclass = CarrierSpecialHandlingDetailType62Sub
# end class CarrierSpecialHandlingDetailType62Sub


class MarksAndNumbersCollectionType63Sub(supermod.MarksAndNumbersCollectionType63):
    def __init__(self, MarksAndNumbersQualifier1=None, MarksAndNumbers1=None):
        super(MarksAndNumbersCollectionType63Sub, self).__init__(MarksAndNumbersQualifier1, MarksAndNumbers1, )
supermod.MarksAndNumbersCollectionType63.subclass = MarksAndNumbersCollectionType63Sub
# end class MarksAndNumbersCollectionType63Sub


class RestrictionsOrConditionsType64Sub(supermod.RestrictionsOrConditionsType64):
    def __init__(self, RestrictionsConditionsQualifier=None, Description=None, QuantityQualifier=None, Quantity1=None, AmountQualifier=None, Amount=None):
        super(RestrictionsOrConditionsType64Sub, self).__init__(RestrictionsConditionsQualifier, Description, QuantityQualifier, Quantity1, AmountQualifier, Amount, )
supermod.RestrictionsOrConditionsType64.subclass = RestrictionsOrConditionsType64Sub
# end class RestrictionsOrConditionsType64Sub


class PackagingType65Sub(supermod.PackagingType65):
    def __init__(self, PackagingCharacteristicCode=None, AgencyQualifierCode=None, PackagingDescriptionCode=None, PackagingDescription=None, UnitLoadOptionCode=None, Measurements=None):
        super(PackagingType65Sub, self).__init__(PackagingCharacteristicCode, AgencyQualifierCode, PackagingDescriptionCode, PackagingDescription, UnitLoadOptionCode, Measurements, )
supermod.PackagingType65.subclass = PackagingType65Sub
# end class PackagingType65Sub


class MeasurementsType66Sub(supermod.MeasurementsType66):
    def __init__(self, MeasurementRefIDCode=None, MeasurementQualifier=None, MeasurementValue=None, CompositeUOM=None, RangeMinimum=None, RangeMaximum=None, MeasurementSignificanceCode=None, MeasurementAttributeCode=None, SurfaceLayerPositionCode=None, IndustryCodeQualifier=None, IndustryCode=None):
        super(MeasurementsType66Sub, self).__init__(MeasurementRefIDCode, MeasurementQualifier, MeasurementValue, CompositeUOM, RangeMinimum, RangeMaximum, MeasurementSignificanceCode, MeasurementAttributeCode, SurfaceLayerPositionCode, IndustryCodeQualifier, IndustryCode, )
supermod.MeasurementsType66.subclass = MeasurementsType66Sub
# end class MeasurementsType66Sub


class MonetaryAmountsType67Sub(supermod.MonetaryAmountsType67):
    def __init__(self, MonetaryAmountCode=None, MonetaryAmount=None, CreditDebitFlag=None):
        super(MonetaryAmountsType67Sub, self).__init__(MonetaryAmountCode, MonetaryAmount, CreditDebitFlag, )
supermod.MonetaryAmountsType67.subclass = MonetaryAmountsType67Sub
# end class MonetaryAmountsType67Sub


class RegulatoryCompliancesType68Sub(supermod.RegulatoryCompliancesType68):
    def __init__(self, RegulatoryComplianceQual=None, YesOrNoResponse=None, RegulatoryComplianceID=None, RegulatoryAgency=None, Description=None):
        super(RegulatoryCompliancesType68Sub, self).__init__(RegulatoryComplianceQual, YesOrNoResponse, RegulatoryComplianceID, RegulatoryAgency, Description, )
supermod.RegulatoryCompliancesType68.subclass = RegulatoryCompliancesType68Sub
# end class RegulatoryCompliancesType68Sub


class SummaryTypeSub(supermod.SummaryType):
    def __init__(self, TotalAmount=None, TotalLineItemNumber=None, Description=None):
        super(SummaryTypeSub, self).__init__(TotalAmount, TotalLineItemNumber, Description, )
supermod.SummaryType.subclass = SummaryTypeSub
# end class SummaryTypeSub


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
        rootTag = 'Orders'
        rootClass = supermod.Orders
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
        rootTag = 'Orders'
        rootClass = supermod.Orders
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
        rootTag = 'Orders'
        rootClass = supermod.Orders
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
        rootTag = 'Orders'
        rootClass = supermod.Orders
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from Orders import *\n\n')
        sys.stdout.write('import Orders as model_\n\n')
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
